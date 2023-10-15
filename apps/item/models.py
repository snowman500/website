# bom models
from extensions.models import *
from extensions.common.base_model import *
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator, MaxLengthValidator



    # # PCB属性
    # pcb1_length = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB长')  
    # pcb1_width = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB宽')
    # pcb1_hight = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB厚度')
    # pcb2_length = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB长')  
    # pcb2_width = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB宽')
    # pcb2_hight = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB厚度')
    # pcb3_length = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB长')  
    # pcb3_width = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB宽')
    # pcb3_hight = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB厚度')
    # pcb4_length = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB长')  
    # pcb4_width = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB宽')
    # pcb4_hight = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB厚度')
    # # 灯珠属性
    # LED_item = DecimalField(max_digits=10, decimal_places=2, verbose_name='灯珠型号')
    # LED_voltage = DecimalField(max_digits=10, decimal_places=2, verbose_name='灯珠电压')
    # LED_current = DecimalField(max_digits=10, decimal_places=2, verbose_name='灯珠电流')
    # LED_power = DecimalField(max_digits=10, decimal_places=2, verbose_name='灯珠功率')
    # # 透镜属性
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='透镜型号')
    # # 连接器属性
    # connect_1 = DecimalField(max_digits=10, decimal_places=2, verbose_name='连接器1')
    # connect_2 = DecimalField(max_digits=10, decimal_places=2, verbose_name='连接器1')
    # connect_3 = DecimalField(max_digits=10, decimal_places=2, verbose_name='连接器1')
    # connect_4 = DecimalField(max_digits=10, decimal_places=2, verbose_name='连接器1')
    # # 辅料属性
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='透镜型号')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='背胶型号')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='反光纸型号')
    # # 包材属性
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='吸塑型号')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='纸箱型号')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='外箱尺寸_长')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='外箱尺寸_宽')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='外箱尺寸_高')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='单箱体积')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='单箱数量')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='单箱重量')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='一条灯条灯珠数量')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='一对灯条灯珠数量')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='一套灯条灯珠数量')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='原厂代码')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='适用模组')
    # price = DecimalField(max_digits=10, decimal_places=2, verbose_name='适用模组')

class WarehouseInfo(BaseModel):
    """仓库信息表"""
    is_active = BooleanField(default=False, verbose_name='启用状态')     # 默认不启用
    warehouse_code = CharField(max_length=50, verbose_name='仓库编码')
    warehouse_name = CharField(max_length=50, verbose_name='仓库名称')
    link_man = CharField(max_length=256, verbose_name='仓库联系人')
    phone_number = CharField(max_length=50, verbose_name='仓库联系人电话')
    province = CharField(max_length=50, verbose_name='省')
    city = CharField(max_length=50, verbose_name='市')
    distrct = CharField(max_length=50, verbose_name='区')
    address = CharField(max_length=50, verbose_name='仓库地址')
#   team = ForeignKey('system.Team', on_delete=CASCADE, related_name='warehouse_info')

    class Meta:
        db_table = 'item_warehouse_info' # 定义属性表名字
        verbose_name = '仓库信息表'
        verbose_name_plural = verbose_name
        
    # WarehouseInfo.objects.create(is_active="1", warehouse_code="001", warehouse_name="深圳仓库", link_man="深圳仓库联系人", phone_number="18806668995", province="广东省",city="深圳市", distrct="宝安区", address="水田社区108工业区")
    # WarehouseInfo.objects.create(is_active="1", warehouse_code="001", warehouse_name="深圳仓库", link_man="深圳仓库联系人", phone_number="18806668995", province="广东省",city="深圳市", distrct="宝安区", address="水田社区108工业区")
    # WarehouseInfo.objects.create(is_active="1", warehouse_code="001", warehouse_name="深圳仓库", link_man="深圳仓库联系人", phone_number="18806668995", province="广东省",city="深圳市", distrct="宝安区", address="水田社区108工业区")
    # WarehouseInfo.objects.create(is_active="1", warehouse_code="001", warehouse_name="深圳仓库", link_man="深圳仓库联系人", phone_number="18806668995", province="广东省",city="深圳市", distrct="宝安区", address="水田社区108工业区")


class WarehouseItem(BaseModel):
    """物料库存表"""
    is_active = BooleanField(default=True, verbose_name='启用状态')     # 默认启用
    product_id = CharField(max_length=50, verbose_name='物料ID')
    w_id = ForeignKey('WarehouseInfo', on_delete=PROTECT,verbose_name='仓库ID', related_name='warehouse_item')
    current_cnt = CharField(max_length=256, verbose_name='库存数量')
    lock_cnt = CharField(max_length=50, verbose_name='锁库数量')
    in_transit_cnt = CharField(max_length=50, verbose_name='在途数量')
#   average_cost = CharField(max_length=50, verbose_name='移动加权成本')
#   team = ForeignKey('system.Team', on_delete=CASCADE, related_name='warehouse_item')

    class Meta:
        db_table = 'item_warehouse_item' # 定义属性表名字
        verbose_name = '物料库存表'
        verbose_name_plural = verbose_name


class ShippingInfo(BaseModel):
    """物流公司信息表"""
    is_active = BooleanField(default=True, verbose_name='启用状态')     # 默认启用
    ship_name = CharField(max_length=50, verbose_name='物流公司名称')
    link_man = CharField(max_length=256, verbose_name='物流公司联系人')
    phone_number = CharField(max_length=50, verbose_name='物流公司联系人电话')
    price  = CharField(max_length=50, verbose_name='价格')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='shipping_info')

    class Meta:
        db_table = 'item_ShippingInfo' # 定义属性表名字
        verbose_name = '物流公司信息表'
        verbose_name_plural = verbose_name



class Supplier(BaseModel):
    """供应商信息表"""
    is_active = BooleanField(default=False, verbose_name='启用状态')     # 默认不启用
    supplier_code = CharField(max_length=10, default='JF0000', verbose_name='启用状态')
    supplier_name = CharField(max_length=50, verbose_name='供应商名称')
    link_man = CharField(max_length=256, verbose_name='联系人')
    phone_number = CharField(max_length=50, verbose_name='联系人电话')
    bank_name = CharField(max_length=50, verbose_name='供应商开户银行名称')
    bank_account = CharField(max_length=50, verbose_name='银行账号')
    address = CharField(max_length=50, verbose_name='供应商地址')
#    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='supplier')
    
    """ 定义了一个save的方法,用于保存模型实例。当保存新的供应商时，
    这个方法会检查是否存在已有的供应商编码。如果存在，则会将新的供应商编码设置为上一个供应商编码加1。
    如果不存在，则会将新的供应商编码设置为"JF0001" """

    def save(self, *args, **kwargs):
        if not self.pk:
            last_supplier = Supplier.objects.all().order_by('id').last()
            if last_supplier:
                last_code = last_supplier.supplier_code
                new_code = 'JF' + str(int(last_code[2:]) + 1).zfill(4)
                self.supplier_code = new_code
        super(Supplier, self).save(*args, **kwargs)



    class Meta:
        db_table = 'item_supplier' # 定义属性表名字
        verbose_name = '供应商信息表'
        verbose_name_plural = verbose_name



# Create your models here.
class ItemCategory(BaseModel):
    """物料类别"""
    # 一级: 0-9
    # 二级--四级: 00-99
    item_id = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], verbose_name='物料分类代码')
    item = CharField(max_length=10, verbose_name='物料名称') 
    parent = ForeignKey('self', null=True, blank=True, on_delete=CASCADE, related_name='item_category', verbose_name='父类别')
#    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='item_category')
    class Meta:
        db_table = 'item_item_category'
        verbose_name = '物料类别'
        verbose_name_plural = verbose_name

class ItemSpecification(BaseModel):
    """物料属性表"""
    is_active = BooleanField(default=True, verbose_name='激活状态') # 默认激活
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='物料价格')
    product_specification = BooleanField(default=False, verbose_name='规格书是否已经上传') # 默认未上传
    supplier = ForeignKey('Supplier', on_delete=PROTECT,verbose_name='供应商名称', related_name='item_specification') # 供应商外键
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
#    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='item_specification')
    spec_1 = CharField(max_length=64, verbose_name='自定义规格1')
    spec_2 = CharField(max_length=64, verbose_name='自定义规格2')
    spec_3 = CharField(max_length=64, verbose_name='自定义规格3')
    spec_4 = CharField(max_length=64, verbose_name='自定义规格4')
    spec_5 = CharField(max_length=64, verbose_name='自定义规格5')
    spec_6 = CharField(max_length=64, verbose_name='自定义规格6')
    spec_7 = CharField(max_length=64, verbose_name='自定义规格7')
    spec_8 = CharField(max_length=64, verbose_name='自定义规格8')
    spec_9 = CharField(max_length=64, verbose_name='自定义规格9')
    spec_10 = CharField(max_length=64, verbose_name='自定义规格10')
    spec_11 = CharField(max_length=64, verbose_name='自定义规格11')
    spec_12 = CharField(max_length=64, verbose_name='自定义规格12')
    spec_13 = CharField(max_length=64, verbose_name='自定义规格13')
    spec_14 = CharField(max_length=64, verbose_name='自定义规格14')
    spec_15 = CharField(max_length=64, verbose_name='自定义规格15')
    spec_16 = CharField(max_length=64, verbose_name='自定义规格16')
    spec_17 = CharField(max_length=64, verbose_name='自定义规格17')
    spec_18 = CharField(max_length=64, verbose_name='自定义规格18')
    spec_19 = CharField(max_length=64, verbose_name='自定义规格19')
    spec_20 = CharField(max_length=64, verbose_name='自定义规格20')

    class Meta:
        db_table = 'item_item_specification'
        verbose_name = '物料属性表'
        verbose_name_plural = verbose_name


class ItemUnit(Model):
    """产品单位"""

    name = CharField(max_length=64, verbose_name='名称')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    #team = ForeignKey('system.Team', on_delete=CASCADE, related_name='item_unit')

    # class Meta:
    #     unique_together = [('name', 'team')]



class ItemSKU(BaseModel):
    '''物料表'''
    is_active = BooleanField(default=True, verbose_name='激活状态') # 默认激活
    is_launched = BooleanField(default=True, verbose_name='是否上架销售') # 默认上架
    type = ForeignKey(ItemCategory, on_delete=CASCADE, verbose_name='物料类型编码', related_name='item_sku')  # 其实是存的GoodsType的id
    goods =CharField(max_length=64, verbose_name='物料型号:JF-D-002')  # 
    item_id = CharField(max_length=20, verbose_name='物料编码:F2.2.09.30.00000')    
    name = CharField(max_length=20, verbose_name='物料名称')
    desc = CharField(max_length=256, verbose_name='物料简介')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='物料价格')
    unite = CharField(max_length=20, verbose_name='物料单位')
    image = ImageField(upload_to='goods', verbose_name='物料图片')
    stock = IntegerField(default=1, verbose_name='物料库存')
    sales = IntegerField(default=0, verbose_name='物料销量')
    brand = DecimalField(max_digits=10, decimal_places=2, verbose_name='灯条品牌')
    set = DecimalField(max_digits=10, decimal_places=2, verbose_name='一套几条')
    enable_inventory_warning = BooleanField(default=False, verbose_name='启用库存警告')
    #team = ForeignKey('system.Team', on_delete=CASCADE, related_name='item_sku')
    
    @classmethod
    def get_number(cls, team):
        default_number = 'F2.2.09.30.00000'
        if instance := cls.objects.filter(team=team).last():
            if result := re.findall('[0-9]+', instance.number):
                current_number = result[-1]
                next_number = str(int(current_number) + 1)

                if len(current_number) > len(next_number):
                    next_number = next_number.zfill(len(current_number))
            else:
                return default_number
        else:
            return default_number
        
        result = re.match(f'^(.*){current_number}(.*?)$', instance.number)
        prefix, suffix = result.group(1), result.group(2)

        return prefix + next_number + suffix
    
    # class Meta:
    #     unique_together = [('item_id', 'team')]
    #     db_table = 'item_item_sku'
    #     verbose_name = '物料'
    #     verbose_name_plural = verbose_name




# class SpecificationOption(BaseModel):
#     """规格选项"""
# #    spec = ForeignKey(SPUSpecification, related_name='options', on_delete=CASCADE, verbose_name='规格')
#     value = CharField(max_length=20, verbose_name='选项值')

#     class Meta:
#         db_table = 'tb_specification_option'
#         verbose_name = '规格选项'
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return '%s - %s' % (self.spec, self.value)


# class SKUSpecification(BaseModel):
#     """SKU具体规格"""
# #    sku = ForeignKey(SKU, related_name='specs', on_delete=CASCADE, verbose_name='sku')
# #    spec = ForeignKey(SPUSpecification, on_delete=PROTECT, verbose_name='规格名称')
#     option = ForeignKey(SpecificationOption, on_delete=PROTECT, verbose_name='规格值')

#     class Meta:
#         db_table = 'tb_sku_specification'
#         verbose_name = 'SKU规格'
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return '%s: %s - %s' % (self.sku, self.spec.name, self.option.value)


