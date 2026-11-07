from django.http import JsonResponse
from rest_framework import generics, permissions

from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer


def home(request):
    return JsonResponse({
        "message": "Social Discovery API is running!",
        "status": "success"
    })


def health_check(request):
    return JsonResponse({
        "status": "healthy"
    })


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')

    data = [
        {
            "id": post.id,
            "username": post.user.username,
            "content": post.content,
            "created_at": post.created_at
        }
        for post in posts
    ]

    return JsonResponse(data, safe=False)


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeCreateAPIView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
