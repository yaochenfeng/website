from django.shortcuts import render
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer


# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=True, url_path='page.html', url_name='post_detail',
            renderer_classes=[renderers.TemplateHTMLRenderer])
    def detail_page(self, request, pk=None):
        obj = self.get_object()
        serializer = self.get_serializer(obj)
        return Response({'serializer': serializer}, template_name='post_detail.html')
