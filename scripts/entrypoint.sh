#!/bin/bash

# 如果有需要，可以等待数据库启动。下面是 PostgreSQL 的一个示例：
#if [ "$DATABASE" = "postgres" ]; then
#    echo "Waiting for PostgreSQL..."
#
#    while ! nc -z $SQL_HOST $SQL_PORT; do
#      sleep 0.1
#    done
#
#    echo "PostgreSQL started"
#fi

# 应用数据库迁移
echo "Applying database migrations..."
python manage.py makemigrations && python manage.py migrate

# 收集静态文件
#echo "Collecting static files..."
python manage.py collectstatic --noinput

# 启动 服务器
echo "Starting server..."
#exec gunicorn --bind 0.0.0.0:8000 website.wsgi:application
exec python manage.py runserver 0.0.0.0:8000