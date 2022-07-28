"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/7/4 17:20
    @File : encrypt.py
"""
from hashlib import md5

from mysitefixed import settings


def my_md5(data_string):
    obj =md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()
