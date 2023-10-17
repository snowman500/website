from django.contrib import admin

# Register your models here.
from .models import *


# 让对应的数据库显示自定义的属性
class ShopSPUAdmin(admin.ModelAdmin):
    list_display = ('id', 'goods_name', 'price', 'desc_detail', 'default_image_url')
    
    

# Register your models here.
admin.site.register(ShopSPU,ShopSPUAdmin)
admin.site.register(ShopImageInfo)
admin.site.register(OrderMaster)
admin.site.register(OrderDetail)
admin.site.register(OrderCart)
admin.site.register(ShopComment)
