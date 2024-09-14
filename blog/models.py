from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Community(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_community")
    name = models.CharField(max_length=500, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class JoinCommunity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    

    class meta:
        unique_together = ('user', 'community') # Prevent duplicate memberships

    def __str__(self):
        return f"{self.user.username} in {self.community.name}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="posts", default=None, null=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug or slugify(self.title) != self.slug:
            # Create slug from the title
            base_slug = slugify(self.title)
            slug = base_slug
            # Ensure the slug is unique
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    def total_votes(self):
        # Use vote_set to count total votes (upvotes minus downvotes)
        upvotes = self.votes.filter(vote_type=Vote.UPVOTE).count()
        downvotes = self.votes.filter(vote_type=Vote.DOWNVOTE).count()
        return upvotes - downvotes
    
class Vote(models.Model):
    UPVOTE = 1
    DOWNVOTE = -1
    VOTE_TYPE_CHOICES = ((UPVOTE, 'Upvote'), (DOWNVOTE, 'Downvote'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='votes', on_delete=models.CASCADE)
    vote_type = models.IntegerField(choices=VOTE_TYPE_CHOICES)

    class Meta:
        unique_together = ('user', 'post')  # Ensures one vote per user per post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.body}"