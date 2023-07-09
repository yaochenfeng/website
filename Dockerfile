# syntax = docker/dockerfile:1.2
ARG IMAGE=python:3.8-slim-buster
FROM ${IMAGE} as app-base
LABEL maintainer="yaochenfeng <yaochenfeng45@gmail.com>"
# python环境
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBUG=false
# 基础依赖
RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && pip install --upgrade pip && pip install poetry \
  && rm -rf /var/lib/apt/lists/*
RUN groupadd -r app && useradd --no-log-init -r -g app app
WORKDIR /app
#python 依赖
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev
COPY . .
ENTRYPOINT ["/app/build.sh"]
CMD gunicorn website.wsgi --bind 0.0.0.0:8000
EXPOSE 8000
HEALTHCHECK CMD curl --fail http://localhost:8000/api || exit 1
