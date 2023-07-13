from django.contrib import admin

from common.admin import BaseModelAdmin
from blog.models import Post

# Register your models here.

admin.site.register(Post, BaseModelAdmin)
