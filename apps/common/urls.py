from django.conf import settings
from django.urls import path, include, re_path
from django.views.static import serve
from django.views.decorators.cache import cache_page
from django.conf import settings
from common import views
from common.routers import router

urlpatterns = [

    path('accounts/profile/', views.profile, name='profile'),
    path('', include('admin_volt.urls')),
]
if not settings.DEBUG:
    urlpatterns += [
        path(f'{settings.STATIC_URL.strip("/")}/<path:path>', serve, {"document_root": settings.STATIC_ROOT}),
        path(f'{settings.MEDIA_URL.strip("/")}/<path:path>', serve, {"document_root": settings.MEDIA_ROOT}),
    ]

router.register(r'users', views.UserViewSet)
