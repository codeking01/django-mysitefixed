import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# 编写视图函数
from myapp.models import UserInfo


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


def info(request):
    # 获取数据库的内容
    data_list = UserInfo.objects.all()
    return render(request, "info.html", {'data_list': data_list})


def addinfo(request):
    if request.method == 'GET':
        return render(request, "addinfo.html")
    # 获取表单的数据
    name = request.POST.get('name')
    password = request.POST.get('password')
    age = request.POST.get('age')

    # 添加数据库的内容
    UserInfo.objects.create(name=name, password=password, age=age)
    return redirect("/info/")


def delinfo(request):
    # 获取请求的参数
    Id = request.GET.get('id')
    # 删除数据库的内容
    UserInfo.objects.filter(id=Id).delete()
    return redirect("/info/")


def editinfo(request):
    if request.method == 'GET':
        # 获取请求的参数
        Id = request.GET.get('id')
        # 获取数据库的内容
        data_list = UserInfo.objects.filter(id=Id).first()
        return render(request, "editinfo.html", {'data_list': data_list})
    # 修改数据
    print(request.POST)
    id = request.POST.get('id')
    name = request.POST.get('name')
    password = request.POST.get('password')
    age = request.POST.get('age')
    UserInfo.objects.filter(id=id).update(name=name, password=password, age=age)
    return redirect("/info/")
