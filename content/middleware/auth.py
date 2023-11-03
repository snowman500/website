from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 0. 排除不需要登录就可以访问的页面
        if request.path_info == "/user/":
            return None
        # 1. 读取当前访问用户的session信息,如果能读到,说明已经登录
        info_dict = request.session.get('info')
        if info_dict:
            return
        # 2. 如果没有登录信息,
        return redirect('/user/')



