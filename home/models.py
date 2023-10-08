from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



# 物料类别
class ItemType(models.Model): 
    is_active = models.BooleanField(default=True, null=True, blank=True,verbose_name="是否可用")
    item = models.CharField(max_length=150, verbose_name="产品") 
    office_supplies = models.CharField(max_length=150, verbose_name="办公用品")
    production_supplies = models.CharField(max_length=150, verbose_name="生产用品")
    def __str__(self):
        return self.name
    
# 物料来源
class Item(models.Model): 
    is_active = models.BooleanField(default=True, null=True, blank=True,verbose_name="是否可用")
    sourcing = models.CharField(max_length=150, verbose_name="采购") 
    self_produced = models.CharField(max_length=150, verbose_name="自制")
    subcontract = models.CharField(max_length=150, verbose_name="委外加工")
    oem = models.CharField(max_length=150, verbose_name="代加工")


    def __str__(self):
        return self.name
    
    # 约束
    # - to是与哪张表关联
    # -to_field,表中的哪一列关联
    # 当外键删除时,此数据对应的外键置空
    depart = models.ForeignKey(to="ItemType", to_field="product",  null=True, blank=True, on_delete=models.SET_NULL)






# 原物料表
# class Material(models.Model): 
#     is_active = models.BooleanField(default=True, null=True, blank=True,verbose_name="是否可用")
#     les = models.CharField(max_length=150, verbose_name="LED 灯珠") 
#     lens = models.CharField(max_length=150, verbose_name="LED 透镜")
#     connector = models.CharField(max_length=150, verbose_name="连接器")
#     pcb = models.CharField(max_length=150, verbose_name="PCB") 
#     SolderPaste = models.CharField(max_length=150, verbose_name="锡膏") 
#     accessories = models.CharField(max_length=150, verbose_name="辅料") 
#     product_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name="产品图片")
#     def __str__(self):
#         return self.name
    
# 成品表
class Material(models.Model): 
    is_active = models.BooleanField(default=True, null=True, blank=True,verbose_name="是否可用")
    spu_id = models.CharField(max_length=150, verbose_name="SPUID") 
    item_name = models.CharField(max_length=150, verbose_name="产品名称")
    detail_description = models.TextField(blank=True, null=True, verbose_name="产品详细描述")    
    price = models.CharField(max_length=150, verbose_name="产品价格") 
    unit = models.CharField(max_length=150, verbose_name="单位") 
    stock = models.CharField(max_length=150, verbose_name="库存") 
    sales_volume = models.CharField(max_length=150, verbose_name="销量") 
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建日期")
    def __str__(self):
        return self.name
# 单位表
class Unit(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    conversion_factor = models.FloatField()

    def __str__(self):
        return self.name
