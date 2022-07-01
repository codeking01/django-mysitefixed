"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/7/1 21:43
    @File : User.py
"""
from django.shortcuts import render, redirect

from myapp.models import UserInfo, Department


def user_list(request):
    # 获取数据库的内容
    UserInfo_list = UserInfo.objects.all()
    # 获取gender
    # UserInfo_list[0].get_gender_display()
    # 获取表关联的内容
    #  UserInfo_list[0].department_id    # 这个是直接获取内容
    # UserInfo_list[0].department.title  # 先获取对象在获取属性
    return render(request, "user_list.html", {'UserInfo_list': UserInfo_list})


def add_user(request):
    if request.method == 'GET':
        context = {
            'gender_choices': UserInfo.gender_choices,
            'department_list': Department.objects.all()
        }
        return render(request, "add_user.html", context)
    # 获取表单的数据
    username = request.POST.get('username')
    password = request.POST.get('password')
    age = request.POST.get('user_age')
    user_account = request.POST.get('user_account')
    user_gender = request.POST.get('user_gender')
    department_id = request.POST.get('department_id')
    create_time = request.POST.get('create_time')
    # 添加到数据库中
    UserInfo.objects.create(name=username, password=password, age=age, account=user_account,
                            gender=user_gender, department_id=department_id, create_time=create_time)
    return redirect('/user_list/')

