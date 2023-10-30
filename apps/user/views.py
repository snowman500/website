from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from django.views.generic import TemplateView

from . import views
from .models import CustomerLogin


# def register(request):

#     return render(request, 'register.html')
# 注册函数
def register(request):
    if request.method=='GET':#若提交的表单为空则让用户重新输入
        return render(request,'register.html')
    if request.method=='POST':
        userid=request.POST.get('username')#取出表单中的用户名
        userpassword=request.POST.get('password')#取出表单中的密码
        try:
            user=CustomerLogin.objects.get(User_id=userid)#在数据库中取出User_id为user_id的对象（由用户名与密码组成）
            if user:
                messages.error(request,'账号已存在')#如果用户名找到了那么提示用户账号已存在并返回登录页面
                return render(request,'login.html')
        except:
            register = CustomerLogin()#定义一个对象（由用户名与密码组成）
            register.User_id = userid
            register.User_passwd = userpassword
            register.save()#将数据保存到数据库中
            messages.error(request,'注册成功') #提示用户注册成功
            return render(request,'login.html') #返回到登录页

# 登录函数
def login(request):
    if request.method=='GET':#如果是空表单让用户从新输入
        return render(request,'login.html')
    if request.method=='POST':
        username=request.POST.get('username')#取出表单中的用户名
        userpassword=request.POST.get('password')#取出表单中的用户密码
        try:
            user=CustomerLogin.objects.get(User_id=username)#在数据库中查找用户名为username的对象（由用户名与密码组成）
            if userpassword==user.User_passwd:#判断密码是否一致
                return HttpResponse('登录成功')#一致则登录成功
            else:
                messages.error(request,'密码错误')#否则提示用户密码错误
                return render(request, 'login.html')#返回让用户重新登录
        except:
            messages.error(request,'账号不存在')#若用户名不存在则提示用户用户不存在
            return render(request,'register.html')#跳转到注册页面让用户注册
