# syntax = docker/dockerfile:1.2
ARG IMAGE=python:3.7-slim-buster
FROM ${IMAGE} as app-base
LABEL maintainer="yaochenfeng <yaochenfeng45@gmail.com>"
# python环境
ENV PYTHONUNBUFFERED=1 \
    DEBUG=false
RUN groupadd -r app && useradd --no-log-init -r -g app app
WORKDIR /app

FROM app-base as builder-base
# 国内加速处理
RUN sed -i 's#http://deb.debian.org#https://mirrors.163.com#g' /etc/apt/sources.list
COPY requirements.txt /app/requirements.txt
RUN --mount=type=cache,target=/root/.cache \
    apt-get update && \
    apt-get -y install libpq-dev gcc && \
    pip install --upgrade pip && pip install --no-cache-dir psycopg2 gunicorn && \
    pip install --no-cache-dir -r /app/requirements.txt
COPY . .
ENTRYPOINT ["/app/build.sh"]
CMD gunicorn website.wsgi --bind 0.0.0.0:8000
