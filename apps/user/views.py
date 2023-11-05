from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, HttpResponse

from .models import CustomerLogin
from content.utils.md5 import md5


def logout(request):
    """ 注销 """
    request.session.clear()
    return redirect('/login/')


class CustomerLoginModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label="Confirm Password",
                                       widget=forms.PasswordInput(render_value=True,
                                                                  attrs={"class": "form-control", "id": "floatingInput",
                                                                         "type": "password",
                                                                         "placeholder": "confirm_password"}))

    # render_value=True, 是为了让两次输入密码不相同的时候,输入框的密码不被清空.
    class Meta:
        model = CustomerLogin
        fields = ["login_email", "user_name", "mobile_phone", "password", "confirm_password"]
        widgets = {
            "login_email": forms.TextInput(
                attrs={"class": "form-control", "id": "floatingInput", "type": "email", "placeholder": "login_email"}),
            "user_name": forms.TextInput(
                attrs={"class": "form-control", "id": "floatingInput", "type": "text", "placeholder": "user_name"}),
            "mobile_phone": forms.TextInput(
                attrs={"class": "form-control", "id": "floatingInput", "type": "text", "placeholder": "Phone number"}),
            "password": forms.PasswordInput(render_value=True,
                                            attrs={"class": "form-control", "id": "floatingInput", "type": "password",
                                                   "placeholder": "Password"}),
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    # 这里是比较两次输入的密码是否一致,不一致弹出报错框,一致则返回确认的密码值
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        return confirm


def register(request):
    """ 添加用户(ModelForm)"""
    if request.method == "GET":
        form = CustomerLoginModelForm()
        return render(request, "register.html", {"form": form})
    if request.method == "POST":
        form = CustomerLoginModelForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['login_email']
            if CustomerLogin.objects.filter(login_email=email).exists():
                return render(request, 'register.html', {'form': form, 'error_message': '账户已经存在'})
            else:
                form.save()
                return redirect('/user/')
        else:
            return render(request, 'register.html', {"form": form})


class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomerLogin

        fields = ["login_email", "password"]
        widgets = {
            "login_email": forms.TextInput(
                attrs={"class": "form-control", "id": "floatingInput", "type": "email", "placeholder": "Email"}),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "id": "floatingInput", "type": "password",
                       "placeholder": "Password"}),
        }

    # 对登录输入的密码进行加密,并返回.
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


def login(request):
    """ 添加用户(ModelForm)"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    # 用户POST提交数据,数据校验
    form = LoginForm(data=request.POST)
    if form.is_valid():
        login_email = form.cleaned_data['login_email']
        password = form.cleaned_data['password']
        user_object = CustomerLogin.objects.filter(login_email=login_email, password=password).first()
        if not user_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, "login.html", {"form": form})

        request.session["info"] = {'id': user_object.id, 'name': user_object.login_email}

        return redirect("/shop/")
    else:
        return render(request, 'login.html', {"form": form})
