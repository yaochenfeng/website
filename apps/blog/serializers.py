from common.serializers import BaseModelSerializer

from blog.models import Post


class PostSerializer(BaseModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
