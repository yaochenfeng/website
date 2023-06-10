from django.contrib.auth.models import User
from rest_framework import serializers

from common.models import UserProfile


class BaseModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    modified_at = serializers.DateTimeField(read_only=True)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = None
        fields = '__all__'
        read_only_fields = ['created_at', 'modified_at', 'created_by']


class ProfileSerializer(BaseModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups', 'profile']
