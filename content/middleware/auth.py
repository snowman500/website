from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, render
from apps.user.models import CustomerLogin


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 0. 排除不需要登录就可以访问的页面
        if request.path_info == "/user/login/":
            return
        if request.path_info == "/user/register/":
            return
        # 1. 读取当前访问用户的session信息,如果能读到,说明已经登录
        info_dict = request.session.get('info')
        # user_id = info_dict.get('id')
        # print(info_dict)
        # print(user_id)
        # user = CustomerLogin.objects.filter(id=user_id).first()
        # print(user)
        if info_dict:
            return
            # return render(request, 'base.html', {'user': user})
        # 2. 如果没有登录信息,重新回到登陆界面
        return redirect('/user/login/')
