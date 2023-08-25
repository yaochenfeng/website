from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve
from django.views.decorators.cache import cache_page
from django.conf import settings
from common import views
from common.routers import router

urlpatterns = [
    path('accounts/profile/', views.profile, name='profile'),
    path('tinymce/', include('tinymce.urls')),
]

router.register(r'users', views.UserViewSet)
