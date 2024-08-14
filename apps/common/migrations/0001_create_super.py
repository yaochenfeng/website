# Generated by Django 5.0.8 on 2024-08-14 15:00
import os

from django.db import migrations
from django.contrib.auth import get_user_model;

def create_default_super(apps, schema_editor):
    # 用户不存在就创建
    User = get_user_model()
    username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin')
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)

class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_default_super),
    ]
