from django.contrib import admin

# Register your models here.
from .models import *


# 让对应的数据库显示自定义的属性
class ShopChannelGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'group_name')
class ShopBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'first_letter', 'url') 
class ShopSKUAdmin(admin.ModelAdmin):
    list_display = ('id', 'goods_name')
class OrderMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_sn', 'shipping_user', 'country','order_money','district_money','shipping_money','payment_money')
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'product_id', 'product_name', 'product_cnt','product_price')
class OrderCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'customer_id', 'product_id', 'product_amount','product_price')
class ShopCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_id', 'order_id', 'customer_id', 'title','content')

# Register your models here.
admin.site.register(ShopChannelGroup,ShopChannelGroupAdmin)
admin.site.register(ShopBrand,ShopBrandAdmin)
admin.site.register(ShopSKU,ShopSKUAdmin)
admin.site.register(OrderMaster,OrderMasterAdmin)
admin.site.register(OrderDetail,OrderDetailAdmin)
admin.site.register(OrderCart,OrderCartAdmin)
admin.site.register(ShopComment,ShopCommentAdmin)
