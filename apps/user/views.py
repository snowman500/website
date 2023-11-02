from django.shortcuts import render, redirect
from django import forms
from .models import CustomerInfo


def login(request):
    return render(request, "login.html")


def logout(request):
    return render(request, "login.html")


def index(request):
    return render(request, "index.html")


class CustomerInfoModelForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ["login_name", "customer_email", "mobile_phone", "password"]
        widgets = {
            "login_name": forms.TextInput(
                attrs={"class": "form-control", "id": "floatingInput", "type": "text", "placeholder": "User name"}),
            "customer_email": forms.TextInput(
                attrs={"class": "form-control", "id": "floatingInput", "type": "email", "placeholder": "User name"}),
            "mobile_phone": forms.TextInput(
                attrs={"class": "form-control", "id": "floatingInput", "type": "text", "placeholder": "User name"}),
            "password": forms.TextInput(
                attrs={"class": "form-control", "id": "floatingInput", "type": "password", "placeholder": "User name"}),
        }





def register(request):
    """ 添加用户(ModelForm)"""
    if request.method == "GET":
        form = CustomerInfoModelForm()
        return render(request, "register.html", {"form": form})

    # 用户POST提交数据,数据校验
    form = CustomerInfoModelForm(data=request.POST)
    if form.is_valid():
        print('form is coming')
        form.save()
        return redirect('/user/register')
    else:
        return render(request, 'register.html', {"form": form})
