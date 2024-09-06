from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Community, JoinCommunity
from .forms import CommunityForm

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"

def post_detail(request, slug, name):
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
    

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
        },
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
    community_posts = Post.objects.filter(status=1, community=community_profile)

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