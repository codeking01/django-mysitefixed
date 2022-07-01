"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/7/1 21:41
    @File : department.py
"""
from django.shortcuts import render, redirect
from myapp.models import Department


def department_list(request):
    # 获取数据库的内容
    Department_list = Department.objects.all()
    return render(request, "depart_list.html", {'Department_list': Department_list})


def add_department(request):
    if request.method == 'GET':
        return render(request, "add_department.html")
    # 获取表单的数据
    title = request.POST.get('department_title')
    # 添加数据库的内容
    Department.objects.create(title=title)
    return redirect("/department_list/")


def del_department_list(request):
    # 获取请求的参数
    Department_id = request.GET.get('nid')
    # 删除数据库的内容
    Department.objects.filter(id=Department_id).delete()
    return redirect("/department_list/")


def edit_department(request, nid):
    if request.method == 'GET':
        # 获取请求的参数
        data_list = Department.objects.filter(id=nid).first()
        return render(request, "editinfo.html", {'data_list': data_list})
    department_title = request.POST.get('department_title')
    # 修改数据
    Department.objects.filter(id=nid).update(title=department_title)
    return redirect("/department_list/")


