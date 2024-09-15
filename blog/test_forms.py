from django.test import TestCase
from .forms import CommentForm, CommunityForm, PostForm

# Create your tests here.
class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid())

    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")

class TestCommunityForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CommunityForm(
            {'name': 'test', 'description': 'This community is about testing'})
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = CommunityForm(
            {'name': '', 'description': 'This community is about testing'})
        self.assertFalse(
            form.is_valid(), msg="Name was not provided, but the form is valid")
        
    def test_description_is_required(self):
        """Test for the 'name' field"""
        form = CommunityForm(
            {'name': 'test', 'description': ''})
        self.assertFalse(
            form.is_valid(), msg="Description was not provided, but the form is valid")
        
class TestPostForm(TestCase):

    def test_form_is_valid(self):
        """Test for all fields"""
        form = PostForm({
            'community': 1,
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'status': 0 
        })
        if not form.is_valid():
            print(form.errors)
        self.assertTrue(form.is_valid(), msg="Form is not valid:")

    def test_community_is_required(self):
        """Test for the 'community' field"""
        form = PostForm({
            'community': '',  
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'status': 0
        })
        self.assertFalse(
            form.is_valid(), msg=f"Community was not provided, but the form is valid: {form.errors}")

    def test_title_is_required(self):
        """Test for the 'title' field"""
        form = PostForm({
            'community': 1,
            'title': '',
            'content': 'This is a test post content.',
            'status': 0
        })
        self.assertFalse(
            form.is_valid(), msg=f"Title was not provided, but the form is valid: {form.errors}")

    def test_content_is_required(self):
        """Test for the 'content' field"""
        form = PostForm({
            'community': 1,
            'title': 'Test Post',
            'content': '',
            'status': 0
        })
        self.assertFalse(
            form.is_valid(), msg=f"Content was not provided, but the form is valid: {form.errors}")

    def test_status_is_required(self):
        """Test for the 'status' field"""
        form = PostForm({
            'community': 1,
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'status': 999
        })
        self.assertFalse(
            form.is_valid(), msg=f"Status was not provided, but the form is valid: {form.errors}")