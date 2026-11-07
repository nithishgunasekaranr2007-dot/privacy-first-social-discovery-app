from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),

    path(
        'posts/',
        views.PostListCreateAPIView.as_view(),
        name='api-posts'
    ),
    path(
        'likes/',
        views.LikeCreateAPIView.as_view(),
        name='api-likes'
    ),
]
