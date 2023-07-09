from django.db import models

from common.models import BaseModel


# Create your models here.
class Post(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
