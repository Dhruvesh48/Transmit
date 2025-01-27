from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Post, Community, Vote, Comment

class TestBlogViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.client.login(username='myUsername', password='myPassword')
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

    def test_edit_post_view(self):
        response = self.client.post(reverse('edit_post', args=['blog-title']), {
            'title': 'Updated Blog title',
            'content': 'Updated Blog content',
            'status': 1
        })
        self.assertEqual(response.status_code, 200)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Blog title')
