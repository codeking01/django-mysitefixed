"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/7/1 21:55
    @File : form.py
"""
from datetime import datetime

from django import forms
from django.core.validators import RegexValidator
from django.forms import ModelForm
from django.views.generic import ListView

from myapp.models import AdminInfo, Task, Orders, City
from myapp.models import UserInfo
from myapp.utils.encrypt import my_md5


# 使用 ModelForm组件实现操作数据功能
class UserModelForm(ModelForm, ListView):
    # paginate_by = 3
    age = forms.CharField(label='年龄', validators=[RegexValidator(r'^\d{1,3}$', '年龄输入有错误！')])
    # name = forms.CharField(min_length=1, label="用户名")
    gender = forms.ChoiceField(label="性别",
                               choices=((1, "男"), (0, "女")),
                               initial=1,
                               widget=forms.widgets.Select())
    create_time = forms.DateTimeField(label='创建时间', initial=datetime.now)

    class Meta:
        model = UserInfo
        fields = '__all__'  # 表示自动渲染所有字段
        # fields = ['id', 'name', 'password', 'age', 'account', 'gender', 'department','create_time']
        widgets = {
            # 'create_time': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(self, *args, **kwargs)
    #     for name, field in self.fields.items():
    #         # print(name, field)
    #         field.widget.attrs = {"class": "form-control", "placeholder": field.label}
    # 加校验 必须是1到2个数字
    # age = forms.IntegerField(label='年纪',validators=[RegexValidator(r'^[1-2]$', '年纪必须是1到2位数字')])

    # 校验年龄
    # def clean_age(self):
    #     age = self.cleaned_data['age']
    #     if age > 999 or age < 1:
    #         raise forms.ValidationError('年龄输入有误！')
    #     return age

    # 校验用户名 (做测试用，假设名字不能重复)
    def clean_name(self):
        the_name = self.cleaned_data['name']
        if UserInfo.objects.exclude(id=self.instance.pk).filter(name=the_name).exists():
            raise forms.ValidationError('用户名已存在！')
        return the_name


# 管理员
class AdminModelForm(ModelForm):
    password = forms.PasswordInput(render_value=True)
    # 新增确认密码字段，但是不存储到数据库
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = AdminInfo
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(render_value=True, attrs={'placeholder': ''}),
        }

    # 数据加密
    def clean_password(self):
        password = self.cleaned_data.get('password')
        return my_md5(password)

    def clean_confirm_password(self):
        confirm_password = my_md5(self.cleaned_data.get('confirm_password'))
        if (self.cleaned_data.get('password') != confirm_password):
            raise forms.ValidationError('密码不一致！')
        # 校验一下密码是否和之前一致，如果一致，让他重新设置
        if (AdminInfo.objects.filter(password=confirm_password)):
            raise forms.ValidationError('密码不能和原密码一致！')


# 登录form
class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    password = forms.CharField(label='密码', max_length=20, required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    # 验证码
    captcha = forms.CharField(label='验证码', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'width': '200px', 'placeholder': '请输入验证码'}))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return my_md5(password)


# form数据
class TaskModelForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'detail': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '请输入任务详情'}),
        }


class order_list(ModelForm):
    class Meta:
        model = Orders
        # fields = '__all__'
        exclude = ["oid", "admin"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入订单名称'}),
        }


# 城市选择
class CityModelForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入城市名称'}),
            'count': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入城市人口'}),
        }