from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Post, Community, Vote, Comment
from .forms import CommentForm

class TestBlogViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.community = Community.objects.create(name="Test Community", description="Test Description", user=self.user)
        self.post = Post.objects.create(
            title="Blog title",
            slug="blog-title",
            content="Blog content",
            status=1,
            user=self.user,
            community=self.community
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')
        self.assertIn(b"Blog title", response.content)

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)

    def test_create_post_view(self):
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.post(reverse('create_post'), {
            'title': 'New Post',
            'content': 'Content of the new post',
            'status': 1,
            'community': self.community.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New Post').exists())

    def test_community_detail_view(self):
        response = self.client.get(reverse('community_detail', args=['Test Community']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/community_detail.html')
        self.assertIn(b"Test Community", response.content)

    def test_create_community_view(self):
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.post(reverse('create_community'), {
            'name': 'New Community',
            'description': 'Description of the new community'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Community.objects.filter(name='New Community').exists())

    def test_vote_post_view(self):
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.get(reverse('vote_post', args=['blog-title', 1]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Vote.objects.filter(user=self.user, post=self.post, vote_type=1).count(), 1)

    def test_edit_post_view(self):
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.post(reverse('edit_post', args=['blog-title']), {
            'title': 'Updated Blog title',
            'content': 'Updated Blog content',
            'status': 1
        })
        self.assertEqual(response.status_code, 200)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Blog title')

    def test_delete_post_view(self):
        self.client.login(username='myUsername', password='myPassword')
        response = self.client.post(reverse('delete_post', args=['blog-title']))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(slug='blog-title').exists())

    def test_comment_edit_view(self):
        comment = Comment.objects.create(user=self.user, post=self.post, body='Initial Comment')
        response = self.client.post(reverse('comment_edit', args=['blog-title', comment.id]), {
            'content': 'Updated Comment'
        })
        self.assertEqual(response.status_code, 302)
        comment.refresh_from_db()
        self.assertEqual(comment.body, 'Initial Comment')

    def test_comment_delete_view(self):
        comment = Comment.objects.create(user=self.user, post=self.post, body='Comment to be deleted')
        response = self.client.post(reverse('comment_delete', args=['blog-title', comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Comment.objects.filter(id=comment.id).exists())

    def test_user_profile_view(self):
        response = self.client.get(reverse('user_profile', args=['myUsername']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/user_profile.html')
        self.assertIn(b"Blog title", response.content)
