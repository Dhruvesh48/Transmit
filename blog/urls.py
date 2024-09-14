from . import views
from django.urls import path

urlpatterns = [
    path('<slug:slug>/delete_comment/<int:comment_id>',views.comment_delete, name='comment_delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>',views.comment_edit, name='comment_edit'),
    path('<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('community/<str:name>/', views.community_detail, name='community_detail'),
    path('create-community/', views.create_community, name='create_community'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/vote/<int:vote_type>/', views.vote_post, name='vote_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('', views.PostList.as_view(), name='home'),
]