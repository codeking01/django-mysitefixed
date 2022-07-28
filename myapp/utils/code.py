# auth: code_king
# time: 2022/7/14 20:54
# file: code.py

# 自定义生成验证码
import random
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from django.http import HttpResponse


def get_color():
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)
    return red, green, blue


def get_code():
    s = '0123456789qwertyuiopasdfghjklzxcvbnmZMXNCBVLASKDJFHGQPOWIERUYT'
    code = ''
    for i in range(4):
        code += random.choice(s)
    return code


def generate_code():
    # 指定画布长宽
    width = 120
    height = 40
    image_size = (width, height)
    # 定义画布
    image = Image.new('RGB', image_size, get_color())
    # 定义画笔
    draw = ImageDraw.Draw(image)
    # 绘制干扰线
    for i in range(10):
        # 指定起始结束位置
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        # 使用画笔绘制，并定义样式颜色等
        draw.line((begin, end), fill=(get_color()))
    # 绘制干扰点
    for i in range(20):
        draw.point((random.randint(0, width), random.randint(0, height)), fill=(get_color()))
    # 产生验证码
    code = get_code()
    # 指定字体和大小
    myfont = ImageFont.truetype(font='static/fonts/arial.ttf', size=30)
    # 逐个绘制字符
    for i in range(4):
        # 每绘制一个，x周位置改变，y可以不变
        distance_x = random.randint(30 * i, 30 * i + 5)
        distance_y = random.randint(0, 5)
        draw.text((distance_x, distance_y), code[i], font=myfont, fill=(get_color()))

    # 滤镜边界加强
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    # 定义一个缓存
    # buffer = BytesIO()
    # 将图片放到缓存
    # image.save(buffer, 'JPEG')
    # 获取缓存内容
    # buf_bytes = buffer.getvalue()
    # 将code保存到session中用于验证
    # request.session['code'] = code
    # return HttpResponse(buf_bytes, 'image/jpeg')
    return image, ''.join(code)