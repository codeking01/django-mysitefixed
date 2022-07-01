import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# 编写视图函数
from myapp.models import UserInfo, Department


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


def department_list(request):
    # 获取数据库的内容
    Department_list = Department.objects.all()
    return render(request, "depart_list.html", {'Department_list': Department_list})


def add_department(request):
    if request.method == 'GET':
        return render(request, "add_department.html")
    # 获取表单的数据
    title = request.POST.get('department_title')
    # 添加数据库的内容
    Department.objects.create(title=title)
    return redirect("/department_list/")


def del_department_list(request):
    # 获取请求的参数
    Department_id = request.GET.get('nid')
    # 删除数据库的内容
    Department.objects.filter(id=Department_id).delete()
    return redirect("/department_list/")


def edit_department(request, nid):
    if request.method == 'GET':
        # 获取请求的参数
        data_list = Department.objects.filter(id=nid).first()
        return render(request, "editinfo.html", {'data_list': data_list})
    department_title = request.POST.get('department_title')
    # 修改数据
    Department.objects.filter(id=nid).update(title=department_title)
    return redirect("/department_list/")


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
