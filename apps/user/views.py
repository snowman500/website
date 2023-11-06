from io import BytesIO

from django.shortcuts import render, redirect, HttpResponse

from content.utils.check_code import check_code
from .modelform import *


def image_code(request):
    """生成图片验证码"""
    # 生成图片 img、数字代码 code，保存在内存中，而不是 Django 项目中
    img, code_string = check_code()

    # 写入到自己的session中(以便于后续获取验证码再进行校验)
    request.session['image_code'] = code_string
    # 给session设置60S超时
    request.session.set_expiry(60)
    # 打印生成的验证码
    print(code_string)

    stream = BytesIO()
    img.save(stream, 'PNG')
    return HttpResponse(stream.getvalue())


def register(request):
    """ 添加用户(ModelForm)"""
    if request.method == "GET":
        form = RegisterModelForm()
        return render(request, "register.html", {"form": form})

    if request.method == "POST":
        form = RegisterModelForm(request.POST)

        if form.is_valid():
            # 验证码的校验
            user_input_code = form.cleaned_data.pop('code')
            code = request.session.get('image_code', "")
            print(code)
            if code.upper() != user_input_code.upper():
                form.add_error("code", "验证码输入错误")
                return render(request, "register.html", {"form": form})

            email = form.cleaned_data['login_email']
            if CustomerLogin.objects.filter(login_email=email).exists():
                return render(request, 'register.html', {'form': form, 'error_message': '账户已经存在'})
            else:
                form.save()
                return redirect('/login/')

        else:
            return render(request, 'register.html', {"form": form})


def login(request):
    """ 添加用户(ModelForm)"""
    if request.method == "GET":
        form = LoginModelForm()
        return render(request, "login.html", {"form": form})

    # 用户POST提交数据,数据校验
    form = LoginModelForm(data=request.POST)
    if form.is_valid():
        # 验证码的校验
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码输入错误")
            return render(request, "login.html", {"form": form})

        login_email = form.cleaned_data['login_email']
        password = form.cleaned_data['password']
        user_object = CustomerLogin.objects.filter(login_email=login_email, password=password).first()
        if not user_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, "login.html", {"form": form})

        request.session["info"] = {'id': user_object.id, 'name': user_object.login_email}
        request.session.set_expiry(60 * 60 * 24)

        return redirect("/shop/")
    else:
        return render(request, 'login.html', {"form": form})


def logout(request):
    """ 注销 """
    request.session.clear()
    return redirect('/login/')


def profile(request):
    """ 用户中心 """

    return render(request, 'profile.html')
