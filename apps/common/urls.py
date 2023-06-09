from django.urls import path, include
from admin_volt import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60 * 15)(views.index), name="index"),
    path('', include('admin_volt.urls')),
]
