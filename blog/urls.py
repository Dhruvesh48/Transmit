from . import views
from django.urls import path

urlpatterns = [
    path('community/<str:name>/', views.community_detail, name='community_detail'),
    path('create-community/', views.create_community, name='create_community'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/vote/<int:vote_type>/', views.vote_post, name='vote_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('', views.PostList.as_view(), name='home'),
]