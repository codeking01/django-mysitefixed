"""mysitefixed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    # 配置路由
    path('index/', views.index),

    path('TemplateInfo/', views.TemplateInfo),

    # 测试一下爬虫模块并且渲染给页面
    path('news/', views.news),

    # 根据数据库的操作info页面
    path('info/', views.info),

    # info的添加
    path('info/add/', views.addinfo),

    # info的删除
    path('info/delete', views.delinfo),

    # info的修改
    path('info/edit/', views.editinfo),
]