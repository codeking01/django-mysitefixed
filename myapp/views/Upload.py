# auth: code_king
# time: 2022/7/27 16:32
# file: Upload.py
from django.shortcuts import render, redirect

from myapp.models import City
from myapp.utils.form import CityModelForm


def files(request):
    if request.method == 'GET':
        # 获取所有城市数据
        queryset = City.objects.all()
        form = CityModelForm()
        context = {
            'queryset': queryset,
            'form': form
        }
        return render(request, 'files.html', context)
    else:
        # print(request.FILES)
        form = CityModelForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            # 对于文件：自动保存；
            # 字段 + 上传路径写入到数据库
            form.save()
            # 重定向到当前页面，浆液门面数据展示
            return redirect('/upload/files/')
    return render(request, 'files.html', {"form": form})