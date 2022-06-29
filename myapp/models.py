from django.db import models

# Create your models here.

# 这个地方操作数据库
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=18)
