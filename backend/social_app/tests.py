from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Like


class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='test12345'
        )

    def test_create_post(self):
        post = Post.objects.create(
            user=self.user,
            content='My first social app post'
        )

        self.assertEqual(post.content, 'My first social app post')
        self.assertEqual(post.user.username, 'testuser')

    def test_create_like(self):
        post = Post.objects.create(
            user=self.user,
            content='Test post'
        )

        like = Like.objects.create(
            user=self.user,
            post=post
        )

        self.assertEqual(like.post, post)
      
