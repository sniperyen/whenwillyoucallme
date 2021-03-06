基于 Django 框架开发的一个网站开发示例，尽量做到可复用，在有新项目时，通过修改相关的网站配置，可以快速的用上。

## 功能列表

* 定时任务和异步： 利用 RabbitMQ+celery，来实现异步功能和定时任务，执行结果存在数据库中
* 网站国际化：不管是后台还是前台的静态文本，都可翻译
* 集成bootstrap3来实现前端页面优化
* 使用xadmin替换了原有简陋的admin
* 使用ace模板系统，美化整体风格

## 同步数据库

在项目中添加了新的model,执行如下命令,在数据库中即可生成对应的表
```
python manage.py makemigrations
python manage.py migrate
```

## 运行方式
```
cd ./MyDjango
python manage.py runserver

```

## 相关地址

* 后台管理系统 http://127.0.0.1:8000/admin   用户名：admin 密码：password
