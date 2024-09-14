from django import forms
from .models import Community, Post, Comment
from django_summernote.widgets import SummernoteWidget

class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'description']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Community.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("A community with this name already exists.")
        return name
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['community', 'title', 'content', 'status']
        widgets = {
            'content': SummernoteWidget(),  # Use Summernote for content
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)