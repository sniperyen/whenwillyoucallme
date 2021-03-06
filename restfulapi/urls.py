from django.conf.urls import patterns, url, include
from rest_framework import routers
from restfulapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'nodes', views.NodeViewSet)
