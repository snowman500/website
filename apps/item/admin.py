from django.contrib import admin
from .models import *


# 让对应的数据库显示自定义的属性
class ItemUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'remark')

class WarehouseInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'warehouse_code', 'warehouse_name', 'link_man', 'phone_number', 'warehouse_name', 'warehouse_name', 'warehouse_name')

class WarehouseItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id', 'w_id', 'current_cnt', 'lock_cnt', 'in_transit_cnt')
    
class ShippingInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ship_name', 'link_man', 'phone_number', 'price')
    
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier_code', 'supplier_name', 'link_man', 'phone_number', 'bank_name', 'bank_account', 'address')
    
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_id', 'item', 'parent')

class ItemSpecificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'product_specification', 'supplier', 'remark', 'spec_1', 'spec_2', 'spec_3', 'spec_4', 'spec_5', 'spec_6')
    
    
class ItemSKUAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_launched', 'type', 'goods', 'item_id', 'name', 'desc', 'price', 'unite', 'image', 'stock', 'sales', 'brand', 'set', 'enable_inventory_warning')
    

    
    
    

# Register your models here.
admin.site.register(WarehouseInfo)
admin.site.register(WarehouseItem)
admin.site.register(ShippingInfo)
admin.site.register(Supplier)
admin.site.register(ItemCategory)
admin.site.register(ItemSpecification)
admin.site.register(ItemUnit,ItemUnitAdmin)
admin.site.register(ItemSKU)
