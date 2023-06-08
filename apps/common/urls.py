from django.conf import settings
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
    path(f'{settings.STATIC_URL.strip("/")}/<path:path>', serve, {"document_root": settings.STATIC_ROOT}),
    path(f'{settings.MEDIA_URL.strip("/")}/<path:path>', serve, {"document_root": settings.MEDIA_ROOT}),
    path('', include('admin_volt.urls')),
]
