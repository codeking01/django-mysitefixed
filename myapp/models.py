from django.db import models


# Create your models here.

# 这个地方操作数据库  添加部门表
class Department(models.Model):
    title = models.CharField(verbose_name='部门名称', max_length=32)

    # 重写 __str__方法
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    # 可以增加verbose_name 相当于增加备注
    name = models.CharField(verbose_name='名字', max_length=10)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    # 在django中可以加约束
    gender_choices = ((1, '男'), (0, '女'))
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    account = models.DecimalField(verbose_name='账户', null=True, max_digits=10, decimal_places=2, default=0)
    # 增加一个创建时间
    # 表关联 这个是级联删除
    department = models.ForeignKey(verbose_name='部门', to=Department, to_field="id", null=True,
                                   on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='入职时间', null=True, blank=True)
