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
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from myapp.views import formerdata, department, User, ModelFormUser, AdminUser, Echarts, Upload

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

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

    # 管理员模块
    path('admin_list/', AdminUser.admin_list),
    path('admin_list/add/', AdminUser.add_admin),
    path('admin_list/<int:nid>/edit/', AdminUser.edit_admin),
    path('admin_list/delete/', AdminUser.del_admin),

    # 登录模块
    path('login/', User.login),
    # 注销模块
    path('logout/', User.logout),
    # 验证码
    path('login/image/code/', User.get_code),

    # 任务管理
    path('tasks/', User.task),
    path('tasks/ajax/', User.task_ajax),
    path('tasks/add/', User.task_add),

    # 订单管理
    path('orders/lists/', User.order),
    path('order/add/', User.order_add),
    path('order/delete/', User.order_delete),
    path('order/edit/', User.order_eidt),

    # echarts 使用
    path('echarts/lists/', Echarts.echarts_lists),
    path('echarts/get_data/', Echarts.echarts_getdata),

    # 文件管理
    path('upload/files/', Upload.files),
]
