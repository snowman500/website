from django.contrib import admin

# Register your models here.
from .models import *


# 让对应的数据库显示自定义的属性
class CustomerLoginAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_activate', 'login_email', 'user_name', 'password', 'mobile_phone')


class CustomerInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_activate', 'gender', 'user_point', 'birthday', 'user_money', 'last_login_time')


# Register your models here.
admin.site.register(CustomerLogin, CustomerLoginAdmin)
admin.site.register(CustomerInfo, CustomerInfoAdmin)
