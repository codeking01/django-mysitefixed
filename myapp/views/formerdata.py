"""
    -- coding: utf-8 --
    @Author: codeking
    @Data : 2022/7/1 21:33
    @File : formerdata.py
"""
import requests
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('欢迎使用！')


# 用户信息，配置html  会现在当前的templates下找，如果找不到回去注册的app的其他的下面找，还有根目录下的templates下的数据
# render会在内部渲染，将数据替换然后给浏览器
def TemplateInfo(request):
    name = "张三",
    role = ['研发部门', '开发部门', '测试部门'],
    person = {'name': '张三', 'age': 18, 'role': '研发部门'}
    return render(request, "TemplateInfo.html", {'name': name, 'role': role, 'person': person})


# 爬取新闻页面，然后渲染到页面
def news(request):
    # 添加fake请求头
    from fake_useragent import UserAgent
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    res = requests.get('http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2022/06/news', headers=headers)
    res = res.json()
    print(res)
    # 获取请求的参数
    print(request.GET)
    return render(request, "news.html", {'res': res})
