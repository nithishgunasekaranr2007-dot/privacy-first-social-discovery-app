
from rest_framework import serializers
from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source='user.username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = ['id', 'user', 'username', 'content', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
      
