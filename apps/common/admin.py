from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile


# Register your models here.
class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'is_active')
    list_display = ('id', 'created_by', '__str__', 'created_at')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


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
