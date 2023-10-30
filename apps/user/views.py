from extensions.common.base_model import BaseModel 
from django.shortcuts import render
from django.shortcuts import redirect
from .models import CustomerInfo
from . import forms
import hashlib

# hash加密
def hash_code(s, salt="mysite"):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def login(request):
    if request.session.get("is_login", None):  # 不允许重复登录
        return redirect("/user/index/")
    if request.method == "POST":
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        login_from = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        # print(username, password)
        # if username.strip() and password:# 确保用户名和密码都不为空
        if login_from.is_valid():
            username = login_from.cleaned_data.get("username")
            password = login_from.cleaned_data.get("password")
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:  # 使用异常处理机制对数据库操作进行判断处理
                user = CustomerInfo.objects.get(name=username)
            except:
                # print("用户不存在！")
                message = "用户不存在！"
                return render(request, "login.html", locals())

            if user.password == hash_code(password):  # 对返回的user对象的password进行判断
                request.session["is_login"] = True
                request.session["user_id"] = user.id
                request.session["user_name"] = user.name
                return redirect("/user/index/")
            else:
                # print("密码错误！")
                message = "密码错误！"
                return render(request, "login.html", locals())
        else:
            return render(request, "login.html", locals())
    # get请求返回空的表单
    login_from = forms.UserForm()
    return render(request, "login.html", locals())


def index(request):
    # 如果未登录访问index,重定向至login
    if not request.session.get("is_login", None):
        return redirect("/user/login/")
    return render(request, "index.html")


def register(request):
    # 如果已经登录，重定向至index
    if request.session.get("is_login", None):
        return redirect("/index/")
    # 判断请求方式为post并进行业务处理
    if request.method == "POST":
        register_form = forms.RegisterFrom(request.POST)  # 定义传过来的表单名称
        message = "请检查填写的内容！"
        if register_form.is_valid():
            login_name = register_form.cleaned_data.get("login_name")
            password1 = register_form.cleaned_data.get("password1")
            password2 = register_form.cleaned_data.get("password2")
            email = register_form.cleaned_data.get("email")
            phone_number = register_form.cleaned_data.get("phone_number")
            gender = register_form.cleaned_data.get("gender")
            # 判断两次密码是否一致
            if password1 != password2:
                message = "两次密码不一致！"
                return render(request, "register.html", locals())
            # 如果一致，判断用户名/邮箱/手机号码是否重复
            else:
                same_name_user = CustomerInfo.objects.filter(name=login_name)
                if same_name_user:
                    message = "用户名已存在！"
                    return render(request, "register.html", locals())
                same_email_user = CustomerInfo.objects.filter(email=email)
                if same_email_user:
                    message = "邮箱已存在！"
                    return render(request, "register.html", locals())
                same_phone_number = CustomerInfo.objects.filter(phone_number=phone_number)
                if same_phone_number:
                    message = "手机号码已存在！"
                    return render(request, "register.html", locals())
                # 保存至数据库
                new_user = CustomerInfo()
                new_user.login_name = login_name
                new_user.password = hash_code(password1)
                new_user.customer_email = email
                new_user.gender = gender
                new_user.mobile_phone = same_phone_number
                new_user.save()
                message = "注册成功！"
                return redirect("/login/")
        else:
            return render(request, "register.html", locals())
    # get请求返回空的表单
    register_form = forms.RegisterFrom()
    return render(request, "register.html", locals())


def logout(request):
    # 如果本来就未登录，也就没有登出一说
    if not request.session.get("is_login", None):
        return redirect("/")
    request.session.flush()  # 删除会话
    return redirect("/")
