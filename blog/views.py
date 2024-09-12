from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Community, JoinCommunity, Vote, Comment
from .forms import CommunityForm, PostForm, CommentForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html" 

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
            print("User: ", request.user)  # Debugging user
            print("Community: ", post_form.cleaned_data.get('community'))
            post.user = request.user  # Associate the post with the current user
            post.save()
            return redirect('community_detail', name=post.community.name)  # Redirect to the community page after posting
    else:
        post_form = PostForm()

    return render(
        request, 
        'blog/create_post.html', 
        {
            'post_form': post_form
        }
    )

def community_detail(request, name):
    """
    Display an individual :model:`blog.Community`.

    **Context**

    ``post``
        An instance of :model:`blog.Community`.

    **Template:**

    :template:`blog/community_detail.html`
    """

    community_profile = get_object_or_404(Community, name=name)
    community_posts = Post.objects.filter(status=1, community=community_profile)
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

from django.shortcuts import get_object_or_404, redirect
from .models import Post, Vote

def vote_post(request, post_id, vote_type):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, id=post_id)
    
    # Validate vote_type
    if vote_type not in ['1', '0']:
        return redirect('post_detail', slug=post.slug)

    vote_type = int(vote_type)
    
    # Check if the user has already voted
    existing_vote = Vote.objects.filter(user=request.user, post=post).first()

    if existing_vote:
        if existing_vote.vote_type == vote_type:
            # Remove the vote if it's the same as before
            existing_vote.delete()
        else:
            # Update the vote to the new type
            existing_vote.vote_type = vote_type
            existing_vote.save()
    else:
        # Create a new vote
        Vote.objects.create(user=request.user, post=post, vote_type=vote_type)

    return render(
        request, 
        'blog/create_post.html', 
        {
            'vote_type': vote_type,
        }
    )

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