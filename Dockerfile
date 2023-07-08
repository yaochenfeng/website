# syntax = docker/dockerfile:1.2
ARG IMAGE=python:3.8-slim-buster
FROM ${IMAGE} as app-base
LABEL maintainer="yaochenfeng <yaochenfeng45@gmail.com>"
# python环境
ENV PYTHONUNBUFFERED=1 \
    DEBUG=false
RUN groupadd -r app && useradd --no-log-init -r -g app app
WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install --upgrade pip && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev
COPY . .
ENTRYPOINT ["/app/build.sh"]
CMD gunicorn website.wsgi --bind 0.0.0.0:8000
