from django.contrib import admin

# Register your models here.
from .models import *


# 让对应的数据库显示自定义的属性
class ShopSPUAdmin(admin.ModelAdmin):
    list_display = ('id', 'goods_name', 'brand', 'listing', 'sales_num','likes_num')
    
    

# Register your models here.
admin.site.register(ShopSPU,ShopSPUAdmin)
admin.site.register(OrderMaster)
admin.site.register(OrderDetail)
admin.site.register(OrderCart)
admin.site.register(ShopComment)
