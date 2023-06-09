import os
import random

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.timezone import now


class BaseModel(models.Model):
    created_at = models.DateTimeField('创建日期', auto_now_add=True)
    updated_at = models.DateTimeField('更新日期', auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name='%(class)s_createdby')

    class Meta:
        abstract = True  # Set this model as Abstract
        ordering = ["-created_at"]


def generate_filename(instance, filename):
    ext = os.path.splitext(filename)[-1].lower()
    name = '{}{}'.format(now().strftime("%Y-%m-%d/%H%M%S"), random.randint(0, 100))
    return 'uploads/{}{}'.format(name, ext)


class UserProfile(BaseModel):
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(default='avatar-default.jpg', upload_to=generate_filename)
    nickname = models.CharField('昵称', max_length=100, blank=True, null=True)
    address = models.CharField('地址', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.created_by.username
