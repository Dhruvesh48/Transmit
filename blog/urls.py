from . import views
from django.urls import path

urlpatterns = [
    path('community/<str:name>/', views.community_detail, name='community_detail'),
    path('create-community/', views.create_community, name='create_community'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('', views.PostList.as_view(), name='home'),
]