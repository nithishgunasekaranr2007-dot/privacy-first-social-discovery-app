from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Social Discovery API is running!",
        "status": "success"
    })


def health_check(request):
    return JsonResponse({
        "status": "healthy"
    })

from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def home(request):
        def post_list(request):
            
        
