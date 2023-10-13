# bom models
from extensions.models import *
from extensions.common.base_model import BaseModel
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator, MaxLengthValidator


class warehouse_info(BaseModel):
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
    creat_time = DateTimeField(auto_now_add = True, verbose_name='创建时间')
    modified_time = DateTimeField(auto_now = True, verbose_name='最后修改时间')
    
    class Meta:
        db_table = 'goods_warehouse_info' # 定义属性表名字
        verbose_name = '仓库信息表'
        verbose_name_plural = verbose_name


class warehouse_product(BaseModel):
    """商品库存表"""
    is_active = BooleanField(default=True, verbose_name='启用状态')     # 默认启用
    product_id = CharField(max_length=50, verbose_name='物料ID')
    w_id = CharField(max_length=50, verbose_name='仓库ID')
    current_cnt = CharField(max_length=256, verbose_name='库存数量')
    lock_cnt = CharField(max_length=50, verbose_name='锁库数量')
    in_transit_cnt = CharField(max_length=50, verbose_name='在途数量')
    average_cost = CharField(max_length=50, verbose_name='移动加权成本')
    creat_time = DateTimeField(auto_now_add = True, verbose_name='创建时间')
    modified_time = DateTimeField(auto_now = True, verbose_name='最后修改时间')

    class Meta:
        db_table = 'goods_warehouse_product' # 定义属性表名字
        verbose_name = '商品库存表'
        verbose_name_plural = verbose_name

class shipping_info(BaseModel):
    """物流公司信息表"""
    is_active = BooleanField(default=True, verbose_name='启用状态')     # 默认启用
    ship_name = CharField(max_length=50, verbose_name='物流公司名称')
    link_man = CharField(max_length=256, verbose_name='物流公司联系人')
    phone_number = CharField(max_length=50, verbose_name='物流公司联系人电话')
    price  = CharField(max_length=50, verbose_name='价格')
    creat_time = DateTimeField(auto_now_add = True, verbose_name='创建时间')
    modified_time = DateTimeField(auto_now = True, verbose_name='最后修改时间')

    class Meta:
        db_table = 'goods_warehouse_product' # 定义属性表名字
        verbose_name = '商品库存表'
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
    creat_time = DateTimeField(auto_now_add = True, verbose_name='创建时间')
    modified_time = DateTimeField(auto_now = True, verbose_name='最后修改时间')
    
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
        db_table = 'f_supplier' # 定义属性表名字
        verbose_name = '供应商信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s - %s' % (self.sku, self.spec.name, self.option.value)


# Create your models here.
class GoodsCategory(BaseModel):
    """物料类别"""
    # 一级: 0-9
    # 二级--四级: 00-99
    item_id = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], verbose_name='物料分类代码')
    item = CharField(max_length=10, verbose_name='物料名称') 
    parent = ForeignKey('self', related_name='subs', null=True, blank=True, on_delete=CASCADE, verbose_name='父类别')

    class Meta:
        db_table = 'f_goods_category'
        verbose_name = '物料类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
    
class GoodsSpecification(BaseModel):
    """物料属性表"""
    is_active = BooleanField(default=True, verbose_name='激活状态') # 默认激活
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    product_specification = BooleanField(default=False, verbose_name='是否已经上传') # 默认未上传
    supplier = ForeignKey('GoodsType', on_delete=CASCADE, verbose_name='商品种类')



    class Meta:
        db_table = 'f_goods_specification'
        verbose_name = '物料属性表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s - %s' % (self.sku, self.spec.name, self.option.value)

    
# 物料表
class GoodsSKU(BaseModel):
    '''物料表'''
    is_active = BooleanField(default=True, verbose_name='激活状态') # 默认激活
    type = ForeignKey('GoodsType', on_delete=CASCADE, verbose_name='商品种类')  # 其实是存的GoodsType的id
    goods = ForeignKey('Goods', on_delete=CASCADE, verbose_name='商品型号:JF-D-002')  # 其实是存的Goods的id
    item_id = CharField(max_length=20, verbose_name='商品编码:F2.2.09.30.00000')    
    name = CharField(max_length=20, verbose_name='商品名称')
    desc = CharField(max_length=256, verbose_name='商品简介')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    unite = CharField(max_length=20, verbose_name='商品单位')
    image = ImageField(upload_to='goods', verbose_name='商品图片')
    stock = IntegerField(default=1, verbose_name='商品库存')
    sales = IntegerField(default=0, verbose_name='商品销量')
    brand = DecimalField(max_digits=10, decimal_places=2, verbose_name='灯条品牌')
    set = DecimalField(max_digits=10, decimal_places=2, verbose_name='一套几条')

# PCB属性

# 物料表
class GoodsSKU(BaseModel):
    '''物料表'''
    is_active = BooleanField(default=True, verbose_name='激活状态') # 默认激活
    type = ForeignKey('GoodsType', on_delete=CASCADE, verbose_name='商品种类')  # 其实是存的GoodsType的id
    goods = ForeignKey('Goods', on_delete=CASCADE, verbose_name='商品型号:JF-D-002')  # 其实是存的Goods的id
    item_id = CharField(max_length=20, verbose_name='商品编码:F2.2.09.30.00000')    
    name = CharField(max_length=20, verbose_name='商品名称')
    desc = CharField(max_length=256, verbose_name='商品简介')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    unite = CharField(max_length=20, verbose_name='商品单位')
    image = ImageField(upload_to='goods', verbose_name='商品图片')
    stock = IntegerField(default=1, verbose_name='商品库存')
    sales = IntegerField(default=0, verbose_name='商品销量')
    brand = DecimalField(max_digits=10, decimal_places=2, verbose_name='灯条品牌')
    set = DecimalField(max_digits=10, decimal_places=2, verbose_name='一套几条')
    # PCB属性
    pcb1_length = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB长')  
    pcb1_width = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB宽')
    pcb1_hight = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB厚度')
    pcb2_length = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB长')  
    pcb2_width = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB宽')
    pcb2_hight = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB厚度')
    pcb3_length = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB长')  
    pcb3_width = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB宽')
    pcb3_hight = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB厚度')
    pcb4_length = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB长')  
    pcb4_width = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB宽')
    pcb4_hight = DecimalField(max_digits=10, decimal_places=2, verbose_name='PCB厚度')
    # 灯珠属性
    LED_item = DecimalField(max_digits=10, decimal_places=2, verbose_name='灯珠型号')
    LED_voltage = DecimalField(max_digits=10, decimal_places=2, verbose_name='灯珠电压')
    LED_current = DecimalField(max_digits=10, decimal_places=2, verbose_name='灯珠电流')
    LED_power = DecimalField(max_digits=10, decimal_places=2, verbose_name='灯珠功率')
    # 透镜属性
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='透镜型号')
    # 连接器属性
    connect_1 = DecimalField(max_digits=10, decimal_places=2, verbose_name='连接器1')
    connect_2 = DecimalField(max_digits=10, decimal_places=2, verbose_name='连接器1')
    connect_3 = DecimalField(max_digits=10, decimal_places=2, verbose_name='连接器1')
    connect_4 = DecimalField(max_digits=10, decimal_places=2, verbose_name='连接器1')
    # 辅料属性
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='透镜型号')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='背胶型号')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='反光纸型号')
    # 包材属性
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='吸塑型号')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='纸箱型号')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='外箱尺寸_长')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='外箱尺寸_宽')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='外箱尺寸_高')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='单箱体积')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='单箱数量')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='单箱重量')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='一条灯条灯珠数量')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='一对灯条灯珠数量')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='一套灯条灯珠数量')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='原厂代码')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='适用模组')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='适用模组')

    enable_inventory_warning = BooleanField(default=False, verbose_name='启用库存警告')
    inventory_upper = FloatField(null=True, verbose_name='库存上限')
    inventory_lower = FloatField(null=True, verbose_name='库存下限')
    
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
    
    class Meta:
        unique_together = [('number', 'team')]
        db_table = 'df_goods_sku'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(BaseModel):
    '''商品图片模型类'''
    sku = ForeignKey('GoodsSKU', on_delete=CASCADE, verbose_name='商品')  # 其实是存的sku的id
    image = ImageField(upload_to='goods', verbose_name='图片路径')

    class Meta:
        db_table = 'df_goods_image'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name


# '首页轮播商品'
class IndexGoodsBanner(BaseModel):
    '''首页轮播商品展示模型类'''
    sku = ForeignKey('GoodsSKU', on_delete=CASCADE, verbose_name='商品')  # 其实是存的sku的id
    image = ImageField(upload_to='banner', verbose_name='图片')
    index = SmallIntegerField(default=0, verbose_name='展示顺序')  # 0 1 2 3

    class Meta:
        db_table = 'df_index_banner'
        verbose_name = '首页轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sku.name


# "主页分类展示商品"
class IndexTypeGoodsBanner(BaseModel):
    '''首页分类商品展示模型类'''
    DISPLAY_TYPE_CHOICES = (
        (0, "标题"),
        (1, "图片")
    )

    type = ForeignKey('GoodsType', on_delete=CASCADE, verbose_name='商品类型')  # 其实是存的GoodsType的id
    sku = ForeignKey('GoodsSKU', on_delete=CASCADE, verbose_name='商品SKU')  # 其实是存的GoodsSKU的id
    display_type = SmallIntegerField(default=1, choices=DISPLAY_TYPE_CHOICES, verbose_name='展示类型')
    index = SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'df_index_type_goods'
        verbose_name = "主页分类展示商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.type.name, self.sku.name)


# "主页促销活动"
class IndexPromotionBanner(BaseModel):
    '''首页促销活动模型类'''
    name = CharField(max_length=20, verbose_name='活动名称')
    url = CharField(max_length=256, verbose_name='活动链接')
    image = ImageField(upload_to='banner', verbose_name='活动图片')  # 去调用FastDfs存储图片
    index = SmallIntegerField(default=0, verbose_name='展示顺序')

    class Meta:
        db_table = 'df_index_promotion'
        verbose_name = "主页促销活动"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
