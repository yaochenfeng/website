# website

django 实现常用 website

## 功能

- docker部署
- celery 异步任务

## 运行

### docker compose 构建运行 --build 重新构建dockerfile

```shell
docker compose up --build
```

## 异步任务

1. django admin 后台管理需要分发定时任务(可选)

```shell
celery -A website beat -l info
```

2. 启动工作节点

```shell
celery -A website worker -E
```

单任务

```shell
celery -A website worker -P solo -l info
 ```