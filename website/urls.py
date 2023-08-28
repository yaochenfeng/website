"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.static import serve

from common.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('accounts/', include('allauth.urls')),
    path("", TemplateView.as_view(template_name="pages/index.html")),
]
if not settings.DEBUG:
    urlpatterns += [
        path(f'{settings.STATIC_URL.strip("/")}/<path:path>', serve, {"document_root": settings.STATIC_ROOT}),
        path(f'{settings.MEDIA_URL.strip("/")}/<path:path>', serve, {"document_root": settings.MEDIA_ROOT}),
    ]
urlpatterns += [
    path('api/', include(router.urls)),
]
