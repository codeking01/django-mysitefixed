# auth: code_king
# time: 2022/7/13 22:00
# file: auth.py
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 如果没有返回值（返回None）,继续向后走,需要放行登录路由
        # 如果有返回值，HttpResponse，render，redirect,则不再向后走
        if request.path_info in ['/login/', '/login/image/code/']:
            return None
        if request.session.get('info') is None:
            return redirect('/login/')
        return None
