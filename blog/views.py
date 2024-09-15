from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Post, Community, JoinCommunity, Vote, Comment
from .forms import CommunityForm, PostForm, CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"

class DraftPostList(generic.ListView):
    queryset = Post.objects.filter(status=0)
    template_name = "blog/user_profile.html"


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.all().count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user  # Associate the post with the current user
            post.save()
            return redirect('community_detail', name=post.community)  # Redirect to the community page after posting
    else:
        post_form = PostForm()

    return render(
        request, 
        'blog/create_post.html', 
        {
            'post_form': post_form,
        }
    )

def community_detail(request, name):
    """
    Display an individual :model:`blog.Community`.

    **Context**

    ``community_profile``
        An instance of :model:`blog.Community`.
    ``community_posts``
        Posts associated with the community.
    ``user_is_member``
        Boolean indicating if the current user is a member of the community.

    **Template:**

    :template:`blog/community_detail.html`
    """

    community_profile = get_object_or_404(Community, name=name)
    community_posts = Post.objects.filter(status=1, community=community_profile)

    # Initialize user_is_member to False by default
    user_is_member = False
    if request.user.is_authenticated:
        user_is_member = JoinCommunity.objects.filter(user=request.user, community=community_profile).exists()
        if request.method == 'POST':
            action = request.POST.get('follow')  # Get the action from the POST request
            if action == "unfollow" and user_is_member:
                # User wants to leave the community, and they are already a member
                JoinCommunity.objects.filter(user=request.user, community=community_profile).delete()
            elif action == "follow" and not user_is_member:
                # User wants to join the community, and they are not yet a member
                JoinCommunity.objects.create(user=request.user, community=community_profile)
            return redirect('community_detail', name=community_profile.name)
    

    return render(
        request,
        "blog/community_detail.html",
        {
            "community_profile": community_profile,
            "user_is_member": user_is_member,
            "community_posts": community_posts
        },
    )

def create_community(request):
    if request.method == 'POST':
        community_form = CommunityForm(request.POST)
        if community_form.is_valid():
            community = community_form.save(commit=False)
            community.user = request.user
            community.save()
            JoinCommunity.objects.create(user=request.user, community=community)
            return redirect('community_detail', name=community.name)
    else:
        community_form = CommunityForm()
    
    return render(
        request, 
        'blog/create_community.html', 
        {
            'community_form': community_form
        }
    )

def vote_post(request, slug, vote_type):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    user = request.user
    
    try:
        vote = Vote.objects.get(user=user, post=post)
        # If the user is trying to vote the same way, remove their vote
        if vote.vote_type == vote_type:
            vote.delete()
        else:
            vote.vote_type = vote_type
            vote.save()
    except Vote.DoesNotExist:
        # Create a new vote if the user hasn't voted on the post yet
        Vote.objects.create(user=user, post=post, vote_type=vote_type)

    return redirect('post_detail', slug=post.slug)

def edit_post(request, slug):
    """
    view to edit posts
    """
    post = get_object_or_404(Post, slug=slug, user=request.user)

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)  # Load the existing post data into the form
        if post_form.is_valid():
            post_form.save()  # Save the edited post
            messages.success(request, "Post updated successfully!")
            return redirect('post_detail', slug=post.slug)  # Redirect to the post detail page
    else:
        post_form = PostForm(instance=post)  # Populate the form with the post data for editing

    return render(request, 'blog/edit_post.html', {'post_form': post_form, 'post': post})

def delete_post(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    if request.user != post.user:
        messages.error(request, "You are not allowed to delete this post.")
        return redirect('post_detail', slug=post.slug)

    # Delete the post
    post.delete()

    # Add a success message
    messages.success(request, "Post deleted successfully.")

    # Redirect back to the post list
    return HttpResponseRedirect(reverse('home'))


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def user_profile(request, username):
    # Get the user by their username
    profile_user = get_object_or_404(User, username=username)
    
    # Fetch all posts made by this user
    user_posts = Post.objects.filter(user=profile_user, status=1).order_by('-created_on')
    user_draft_posts = Post.objects.filter(user=profile_user, status=0).order_by('-created_on')

    # Pass the posts and user to the template
    return render(request, 'blog/user_profile.html', {
        'profile_user': profile_user,
        'user_posts': user_posts,
        'user_draft_posts': user_draft_posts
    })