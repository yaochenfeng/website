import os
import random

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
from django.utils.timezone import now


class BaseModel(models.Model):
    created_at = models.DateTimeField('创建日期', auto_now_add=True)
    updated_at = models.DateTimeField('更新日期', auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                   related_name='%(class)s_createdby')
    is_active = models.BooleanField('激活状态', default=True)

    class Meta:
        abstract = True  # Set this model as Abstract
        ordering = ["-created_at"]

    def get_absolute_url(self):
        model_name = self.__class__.__name__.lower()
        return reverse(f'{model_name}_detail', args=[self.id])

    def save(self, *args, **kwargs):
        if not self.id:
            # 新创建的对象，设置 created_by 字段
            if not self.pk and 'user' in kwargs:
                self.created_by = kwargs.pop('user', None)
        super().save(*args, **kwargs)

    def soft_delete(self):
        """
            软删除.
        """
        self.is_active = False
        self.save()

    # 激活
    def activate(self):
        self.is_active = True
        self.save()


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
