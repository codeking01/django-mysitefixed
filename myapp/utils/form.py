"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/7/1 21:55
    @File : form.py
"""

from django.forms import ModelForm

from myapp.models import UserInfo


# 使用 ModelForm组件实现操作数据功能
class UserModelForm(ModelForm):
    # name = forms.CharField(min_length=1, label="用户名")
    class Meta:
        model = UserInfo
        fields = '__all__'  # 表示自动渲染所有字段
        # fields = ['id', 'name', 'password', 'age', 'account', 'gender', 'department','create_time']

    # def __init__(self, *args, **kwargs):
    # super().__init__(self, *args, **kwargs)
    #     for name, field in self.fields.items():
    #         # print(name, field)
    #         field.widget.attrs = {"class": "form-control", "placeholder": field.label}
