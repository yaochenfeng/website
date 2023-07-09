from django.shortcuts import render
from rest_framework import viewsets

from blog.models import Post
from blog.serializers import PostSerializer


# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()
