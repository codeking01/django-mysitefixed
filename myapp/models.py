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

    def __str__(self):
        return self.name


# 创建管理员
class AdminInfo(models.Model):
    name = models.CharField(verbose_name='管理员名称', max_length=10)
    password = models.CharField(verbose_name='管理员密码', max_length=64)

    def __str__(self):
        return self.name


# 任务管理
class Task(models.Model):
    """ 任务 """
    level_choices = ((1, '普通'), (2, '紧急'), (3, '非常紧急'))
    level = models.SmallIntegerField(verbose_name='紧急程度', choices=level_choices, default=1)
    title = models.CharField(verbose_name='任务名称', max_length=32)
    detail = models.TextField(verbose_name='任务详情')
    user = models.ForeignKey(verbose_name='用户', to=UserInfo, to_field="id", null=True, on_delete=models.CASCADE)


class Orders(models.Model):
    """订单"""
    oid = models.CharField(verbose_name='订单编号', null=False, max_length=32,primary_key=True)
    title = models.CharField(verbose_name='订单名称', max_length=32)
    price = models.FloatField(verbose_name="价格")
    status_choices = ((1, '未支付'), (2, '已支付'), (3, '已取消'))
    status = models.SmallIntegerField(verbose_name='订单状态', choices=status_choices, default=1)
    admin = models.ForeignKey(verbose_name='用户', to="AdminInfo", to_field="id", null=True, on_delete=models.CASCADE)

class City(models.Model):
    """城市"""
    name = models.CharField(verbose_name='城市名称', max_length=32)
    count=models.IntegerField(verbose_name='城市人数',max_length=32)
    img=models.FileField(verbose_name='城市图片',upload_to='city')
    def __str__(self):
        return self.name