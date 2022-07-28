"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/7/4 11:19
    @File : AdminUser.py
"""

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from myapp.models import AdminInfo
from myapp.utils.form import AdminModelForm


def admin_list(request):
    # 获取请求的参数
    q = request.GET.get('q')
    # 当q不为空时
    if q != 'None' and q is not None:
        dict_data = {}
        the_value = request.GET.get('q').encode('utf-8').decode('utf-8')
        if the_value:
            dict_data['name__contains'] = the_value
        queryset = AdminInfo.objects.filter(**dict_data)
    else:
        queryset = AdminInfo.objects.all().order_by('id')
    paginator = Paginator(queryset, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_list.html', {'page_obj': page_obj, 'q': q})


def add_admin(request):
    if request.method == 'GET':
        admin_form = AdminModelForm()
        return render(request, 'admin_add.html', {'admin_form': admin_form})
    admin_form = AdminModelForm(request.POST)
    if admin_form.is_valid():
        admin_form.save()
        return redirect('/admin_list/')
    else:
        return render(request, 'admin_add.html', {'admin_form': admin_form})


def edit_admin(request, nid):
    if request.method == 'GET':
        # 获取请求的参数
        data_list = AdminInfo.objects.filter(id=nid).first()
        # instance可以让它取出这一行的数据
        admin_form = AdminModelForm(instance=data_list)
        # 将密码置空
        # admin_form.initial['password'] = ''
        return render(request, 'admin_edit.html', {'admin_form': admin_form})
    admin_form = AdminModelForm(request.POST, instance=AdminInfo.objects.get(id=nid))
    if admin_form.is_valid():
        admin_form.save()
        return redirect('/admin_list/')
    else:
        return render(request, 'admin_edit.html', {'admin_form': admin_form})


def del_admin(request):
    # 获取请求的参数
    admin_id = request.GET.get('nid')
    # 删除数据库的内容
    AdminInfo.objects.filter(id=admin_id).delete()
    return redirect("/admin_list/")
