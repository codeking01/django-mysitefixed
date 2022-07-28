# auth: code_king
# time: 2022/7/27 15:15
# file: Echarts.py
from django.http import JsonResponse
from django.shortcuts import render


def echarts_lists(request):
    return render(request, 'echarts_lists.html')


def echarts_getdata(request):
    # 写死数据，后期可以从数据库获取
    data = {
        'status': True,
        'series': [
            {
                'name': '销量',
                'type': 'bar',
                'data': [5, 20, 36, 10, 10, 80]
            },
            {
                'name': '退货',
                'type': 'bar',
                'data': [15, 80, 36, 10, 10, 10]
            }
        ],
        'xAxis': ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子'],
        'legend': ['销量', '退货']
    }
    return JsonResponse(data)
