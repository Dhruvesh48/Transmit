from django.test import TestCase
from .forms import CommentForm, CommunityForm, PostForm
from .models import Community

class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        """Test that the form is valid with a valid body."""
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid())

    def test_form_is_invalid(self):
        """Test that the form is invalid with an empty body."""
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form should be invalid with an empty body.")


class TestCommunityForm(TestCase):

    def test_form_is_valid(self):
        """Test that the CommunityForm is valid with all fields."""
        form = CommunityForm(
            {'name': 'test', 'description': 'This community is about testing'})
        self.assertTrue(form.is_valid(), msg="CommunityForm should be valid with all required fields.")

    def test_name_is_required(self):
        """Test that the 'name' field is required."""
        form = CommunityForm(
            {'name': '', 'description': 'This community is about testing'})
        self.assertFalse(
            form.is_valid(), msg="Form should be invalid when 'name' is empty.")

    def test_description_is_required(self):
        """Test that the 'description' field is required."""
        form = CommunityForm(
            {'name': 'test', 'description': ''})
        self.assertFalse(
            form.is_valid(), msg="Form should be invalid when 'description' is empty.")


class TestPostForm(TestCase):

    def test_form_is_valid(self):
        """Test that the PostForm is valid with all fields."""
        form = PostForm({
            'community': 'python',
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'status': 0
        })
        self.assertFalse(form.is_valid(), msg=f"Form should be valid. Errors: {form.errors}")

    def test_community_is_required(self):
        """Test that the 'community' field is required."""
        form = PostForm({
            'community': '',
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'status': 0
        })
        self.assertFalse(
            form.is_valid(), msg=f"Form should be invalid without 'community'. Errors: {form.errors}")

    def test_title_is_required(self):
        """Test that the 'title' field is required."""
        form = PostForm({
            'community': 'python',
            'title': '',
            'content': 'This is a test post content.',
            'status': 0
        })
        self.assertFalse(
            form.is_valid(), msg=f"Form should be invalid without 'title'. Errors: {form.errors}")

    def test_content_is_required(self):
        """Test that the 'content' field is required."""
        form = PostForm({
            'community': 'python',
            'title': 'Test Post',
            'content': '',
            'status': 0
        })
        self.assertFalse(
            form.is_valid(), msg=f"Form should be invalid without 'content'. Errors: {form.errors}")

    def test_status_is_invalid(self):
        """Test that the 'status' field must be within the expected choices."""
        form = PostForm({
            'community': 'python',
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'status': 999
        })
        self.assertFalse(
            form.is_valid(), msg=f"Form should be invalid with an incorrect 'status'. Errors: {form.errors}")
