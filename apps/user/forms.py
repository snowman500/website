from django.forms import ModelForm
from django.forms import widgets
from .models import CustomerLogin
from django.core.exceptions import ValidationError
 
 
class CustomerLoginModelForm(ModelForm):
    class Meta:
        model = CustomerLogin
        fields = "__all__"
        # fields = ["name", "age"]  # 只校验名字和年龄
        # exclude = ["create_time"]  # 除了建立时间其他的都要校验
        labels = {"login_name": "login_name", "customer_email": "customer_email", "password": "password", "re_password": "re_password"}
        widgets = {
            # 不同类型的字段要用不同的属性输出，不然表单的格式验证失效
            # 给不同字段添加class属性，改变样式
            "login_name": widgets.TextInput({"class": "form-control"}),
            "password": widgets.NumberInput({"class": "form-control"}),
            "re_password": widgets.DateInput({"class": "form-control", "type": "date"}),  # 自己给type属性让前端模板有date样式
            "customer_email": widgets.EmailInput({"class": "form-control"}),
        }
        # 自定义插件
        widgets = None
        from django.forms import widgets as wid
        # widgets = {
        #     'content': wid.Textarea()
        # }

        # 自定义错误信息
        error_messages = {
            'login_name': {'required': '标题不能为空'},
            'password': {'required': '内容不能为空'},
            're_password': {'required': '作者不能为空'},
            "customer_email": {"invalid": "请填写正确的邮箱格式"}
        }
        # 给错误改中文
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key, message_dicts in errors.items():
            messages = []
            for message in message_dicts:
                messages.append(message['message'])
            new_errors[key] = messages
        return new_errors


