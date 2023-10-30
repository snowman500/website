from django import forms
from .models import CustomerInfo, CustomerLogin
#from captcha.fields import CaptchaField


# class UserForm(forms.Form):
#     username = forms.CharField(label="用户名",max_length=128,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': "Username",'autofocus': ''}))
#     password = forms.CharField(label="密码",max_length=256,widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))
#     #captcha = CaptchaField(label="验证码")

# class RegisterFrom(forms.Form):
#     gender = (
#         ('male', "男"),
#         ('female', "女"),
#     )
#     username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     password2 = forms.CharField(label="确认密码", max_length=256,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     sex = forms.ChoiceField(label='性别', choices=gender)
#     #captcha = CaptchaField(label='验证码')
class UserForm(forms.ModelForm):
    class Meta:
        model = CustomerLogin
        fields = "__all__"  # 字段，如果是__all__,就是表示列出所有的字段
        exclude = None  # 排除的字段
        # 提示信息
        labels = {
            'login_name': '用户名',
            'password': '密码',
        }
        help_texts = None  # 帮助提示信息

        # 自定义插件
        widgets = None
        from django.forms import widgets as wid
        # widgets = {
        #     'content': wid.Textarea()
        # }

        # 自定义错误信息
        error_messages = {
            'login_name': {'required': '用户名不能为空'},
            'password': {'required': '密码不能为空'},
        }

    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key, message_dicts in errors.items():
            messages = []
            for message in message_dicts:
                messages.append(message['message'])
            new_errors[key] = messages
        return new_errors


class RegisterFrom(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = "__all__"  # 字段，如果是__all__,就是表示列出所有的字段
        exclude = None  # 排除的字段
        # 提示信息
        labels = {
            'username': '用户名',
            'password1': '密码',
            'password2': '确认密码',
            'email': '邮箱地址',
            'sex': '性别',
        }
        help_texts = None  # 帮助提示信息

        # 自定义插件
        widgets = None
        from django.forms import widgets as wid
        # widgets = {
        #     'content': wid.Textarea()
        # }

        # 自定义错误信息
        # error_messages = {
        #     'title': {'required': '标题不能为空'},
        #     'content': {'required': '内容不能为空'},
        #     'author': {'required': '作者不能为空'}
        # }

    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key, message_dicts in errors.items():
            messages = []
            for message in message_dicts:
                messages.append(message['message'])
            new_errors[key] = messages
        return new_errors