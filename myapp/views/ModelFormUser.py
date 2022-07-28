"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/7/1 21:45
    @File : ModelFormUser.py
"""
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from myapp.models import UserInfo
from myapp.utils.form import UserModelForm


def User_molelform(request):
    # 获取请求的参数
    q = request.GET.get('q')
    if q != 'None' and q is not None:
        dict_data = {}
        the_value = request.GET.get('q').encode('utf-8').decode('utf-8')
        if the_value:
            dict_data['name__contains'] = the_value
        queryset = UserInfo.objects.filter(**dict_data)
        # UserInfo_list = UserInfo.objects.all().order_by('id')
        # 获取请求的参数
        # user_form=UserModelForm(instance=UserInfo_list)
        # return render(request, "user_modelform.html", {'UserInfo_list': queryset})
    else:
        queryset = UserInfo.objects.all().order_by('id')
    paginator = Paginator(queryset, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "user_modelform.html", {'page_obj': page_obj, 'q': q})


def ModelUser_add(request):
    if request.method == 'GET':
        user_form = UserModelForm()
        return render(request, 'user_model_add.html', {'user_form': user_form})
    user_form = UserModelForm(request.POST)
    if user_form.is_valid():
        user_form.save()
        return redirect('/modelform_userinfo/')
    else:
        return render(request, 'user_model_add.html', {'user_form': user_form})


def del_user(request):
    # 获取请求的参数
    User_id = request.GET.get('nid')
    # 删除数据库的内容
    UserInfo.objects.filter(id=User_id).delete()
    return redirect("/modelform_userinfo/")


def edit_user(request, nid):
    if request.method == 'GET':
        # 获取请求的参数
        data_list = UserInfo.objects.filter(id=nid).first()
        # instance可以让它取出这一行的数据
        user_form = UserModelForm(instance=data_list)
        return render(request, 'user_model_edit.html', {'user_form': user_form})
    user_form = UserModelForm(request.POST, instance=UserInfo.objects.get(id=nid))
    if user_form.is_valid():
        user_form.save()
        return redirect('/modelform_userinfo/')
    else:
        return render(request, 'user_model_edit.html', {'user_form': user_form})
