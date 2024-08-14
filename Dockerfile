# 使用官方Python基础镜像
FROM python:3.12-slim

ENV HOME=/home/app \
    APP_HOME=/home/app/web

RUN mkdir -p $APP_HOME && \
    addgroup --system app && adduser --system --group app

WORKDIR $APP_HOME
COPY ./scripts/entrypoint.sh /home/app/entrypoint.sh
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
# copy project
COPY . $APP_HOME
RUN chown -R app:app $APP_HOME && \
    chmod +x  $HOME/entrypoint.sh

# change to the app user
USER app
## 暴露Django默认端口
EXPOSE 8000
ENTRYPOINT ["/home/app/entrypoint.sh"]
