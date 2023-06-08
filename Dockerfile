# syntax = docker/dockerfile:1.2

FROM python:3.7-slim-buster
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN sed -i 's#http://deb.debian.org#https://mirrors.163.com#g' /etc/apt/sources.list
RUN --mount=type=cache,target=/root/.cache \
    apt-get update && \
    apt-get -y install libpq-dev gcc && \
    pip install --upgrade pip && pip install psycopg2 gunicorn && \
    pip install -r /app/requirements.txt


COPY . .
ENTRYPOINT ["/app/build.sh"]
CMD gunicorn website.wsgi --bind 0.0.0.0:8000
