from django.db import models
from django.urls import reverse

from common.models import BaseModel


# Create your models here.
class Post(BaseModel):
    title = models.CharField('文章标题', max_length=200)
    content = models.TextField('文章正文')
    total_views = models.PositiveIntegerField('文章浏览量', default=0)

    def __str__(self):
        return self.title
