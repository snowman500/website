from django import forms
from django.core.exceptions import ValidationError

from content.utils.md5 import md5
from .models import CustomerLogin


class LoginModelForm(forms.ModelForm):
    code = forms.CharField(label="CAPTCHA",
                           widget=forms.PasswordInput(
                               attrs={"class": "form-control", "id": "floatingInput", "type": "text",
                                      "placeholder": "CAPTCHA"}))

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


class RegisterModelForm(forms.ModelForm):
    confirm_password = forms.CharField(label="Confirm Password",
                                       widget=forms.PasswordInput(render_value=True,
                                                                  attrs={"class": "form-control", "id": "floatingInput",
                                                                         "type": "password",
                                                                         "placeholder": "confirm_password"}))
    code = forms.CharField(label="CAPTCHA",
                           widget=forms.PasswordInput(
                               attrs={"class": "form-control", "id": "floatingInput", "type": "text",
                                      "placeholder": "CAPTCHA"}))

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
