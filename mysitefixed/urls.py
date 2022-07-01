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
# from django.contrib import admin
from django.urls import path

from myapp.views import formerdata, department, User, ModelFormUser

urlpatterns = [
    # path('admin/', admin.site.urls),

    # 配置路由
    path('index/', formerdata.index),
    path('TemplateInfo/', formerdata.TemplateInfo),
    # 测试一下爬虫模块并且渲染给页面
    path('news/', formerdata.news),

    # 根据数据库的操作info页面
    path('department_list/', department.department_list),
    # info的添加
    path('department_list/add/', department.add_department),
    # info的删除
    path('department_list/delete/', department.del_department_list),
    # info的修改
    path('department_list/<int:nid>/edit/', department.edit_department),

    # 用户的路由
    path('user_list/', User.user_list),
    path('user_list/add/', User.add_user),

    # 使用 ModelForm 完成用户管理
    path('modelform_userinfo/', ModelFormUser.User_molelform),
    # 增加用户
    path('modelform_userinfo/add/', ModelFormUser.ModelUser_add),
    # 删除用户
    path('modelform_userinfo/delete/', ModelFormUser.del_user),
    # 修改用户
    path('modelform_userinfo/<int:nid>/edit/', ModelFormUser.edit_user),
]
