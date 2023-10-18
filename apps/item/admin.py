from django.contrib import admin
from .models import *


# 让对应的数据库显示自定义的属性
class WarehouseInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'warehouse_code', 'warehouse_name', 'link_man', 'phone_number', 'province', 'city', 'distrct', 'address')
    
class ShippingInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ship_name', 'link_man', 'phone_number', 'price')
    
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier_code', 'supplier_name', 'link_man', 'phone_number', 'bank_name', 'bank_account', 'address')
    
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_id', 'item', 'parent')

class ItemSpecificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_id',  'remark', 'spec_1', 'spec_2', 'spec_3', 'spec_4', 'spec_5', 'spec_6')
    
class ItemSKUAdmin(admin.ModelAdmin):
    list_display = ('id', 'spec', 'goods', 'item_id', 'name', 'desc', 'price', 'unite', 'current_cnt', 'sales', 'supplier')
 
class ItemUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'remark')   

# Register your models here.
admin.site.register(WarehouseInfo,WarehouseInfoAdmin)
admin.site.register(ShippingInfo,ShippingInfoAdmin)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(ItemCategory,ItemCategoryAdmin)
admin.site.register(ItemSpecification,ItemSpecificationAdmin)
admin.site.register(ItemUnit,ItemUnitAdmin)
admin.site.register(ItemSKU,ItemSKUAdmin)
