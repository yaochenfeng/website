from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile


# Register your models here.

class UserProfileAdmin(admin.StackedInline):
    model = UserProfile
    can_delete = False
    fk_name = "created_by"


class UserAdmin(AuthUserAdmin):
    inlines = [UserProfileAdmin]


# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin)
