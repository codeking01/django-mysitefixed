"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/7/1 21:43
    @File : User.py
"""
import json
import time
from io import BytesIO

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from myapp.models import UserInfo, Department, AdminInfo, Task, Orders
from myapp.utils.code import generate_code
from myapp.utils.form import LoginForm, TaskModelForm, order_list


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


def login(request):
    if request.method == 'GET':
        # 获取表单form 转至页面
        form = LoginForm()
        return render(request, "login.html", {'form': form})
    form = LoginForm(request.POST)
    if form.is_valid():
        # 数据库校验 可以用字典的形式，然后解包
        # admin_obj = AdminInfo.objects.filter(**form.cleaned_data).first()
        admin_obj = AdminInfo.objects.filter(name=form.cleaned_data['username'],
                                             password=form.cleaned_data['password']).first()
        user_input_code = form.cleaned_data.pop('captcha')
        code = request.session['image_code']
        if user_input_code.lower() != code.lower():
            form.add_error('captcha', '验证码错误')
            return render(request, "login.html", {'form': form})
        if admin_obj is None:
            form.add_error('password', '用户名或密码错误')
            return render(request, 'login.html', {'form': form})
        # 记录登录状态
        request.session['info'] = {'id': admin_obj.id, 'username': admin_obj.name}
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect('/user_list/')
    return render(request, 'login.html', {'form': form})


def logout(request):
    # 清除登录状态
    request.session.clear()
    return redirect('/login/')


def get_code(request):
    image, code = generate_code()
    # 定义一个缓存
    buffer = BytesIO()
    # 将图片放到缓存
    image.save(buffer, 'png')
    # 获取缓存内容
    buf_bytes = buffer.getvalue()
    # 将code保存到session中用于验证,并且设置过期时间
    request.session['image_code'] = code
    request.session.set_expiry(300)
    return HttpResponse(buf_bytes, content_type='image/png')


def task(request):
    queryset = Task.objects.all().order_by('-id')
    form = TaskModelForm()
    context = {
        'queryset': queryset,
        'form': form
    }
    # 任务列表
    return render(request, 'task.html', context)


@csrf_exempt
def task_ajax(request):
    print(request.POST)
    data_dict = {"status": 200, 'data': [1, 2, 3, 4]}
    return HttpResponse(json.dumps(data_dict))


@csrf_exempt
def task_add(request):
    # print(request.POST)
    form_add = TaskModelForm(data=request.POST)
    if form_add.is_valid():
        form_add.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    data_dict = {"status": False, 'errors': form_add.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))


@csrf_exempt
def order(request):
    queryset = Orders.objects.all().order_by('admin_id')
    form = order_list()
    context = {
        'queryset': queryset,
        'form': form
    }
    return render(request, 'order.html', context)


@csrf_exempt
def order_add(request):
    # 判断一下是编辑还是添加
    oid = request.GET.get('edit_oid')
    if oid !='undefined':
        # 编辑
        order_obj = Orders.objects.get(oid=oid)
        form = order_list(request.POST,instance=order_obj)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": True})
        return JsonResponse({"status": False, "errors": form.errors})
    else:
        """ 新建订单 """
        form = order_list(data=request.POST)
        if form.is_valid():
            # 从session中获取当前用户
            form.instance.admin_id = request.session.get('info').get('id')
            # 生产订单编号
            form.instance.oid = str(
                time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + str(time.time()).replace('.', '')[-7:])
            form.save()
            return JsonResponse({"status": True})
        return JsonResponse({"status": False, "errors": form.errors})


def order_delete(request):
    """ 删除订单 """
    oid = request.GET.get('del_oid')
    # 删除订单,判断是否存在
    if Orders.objects.filter(oid=oid).exists():
        Orders.objects.filter(oid=oid).delete()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, "errors": "订单不存在,点击刷新页面！"})


def order_eidt(request):
    """ 订单编辑 """
    oid = request.GET.get('edit_oid')
    if Orders.objects.filter(oid=oid).exists():
        edit_data=Orders.objects.filter(oid=oid).values('oid', 'title', 'price', 'status', 'admin_id').first()
        return JsonResponse({"status": True, "edit_data": edit_data})
    return JsonResponse({"status": False, "errors": "订单不存在,点击刷新页面！"})
