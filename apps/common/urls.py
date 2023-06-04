import admin_volt.views
from django.urls import path, include

urlpatterns = [
    path('', include('admin_volt.urls')),
]
