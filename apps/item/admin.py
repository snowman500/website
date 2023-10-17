from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(WarehouseInfo)
admin.site.register(WarehouseItem)
admin.site.register(ShippingInfo)
admin.site.register(Supplier)
admin.site.register(ItemCategory)
admin.site.register(ItemSpecification)
admin.site.register(ItemUnit)
admin.site.register(ItemSKU)
