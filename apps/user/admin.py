from django.contrib import admin

# Register your models here.
from .models import *


# 让对应的数据库显示自定义的属性
class CustomerInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_activate', 'login_name', 'password', 'customer_email', 'mobile_phone')


# Register your models here.
admin.site.register(CustomerInfo, CustomerInfoAdmin)