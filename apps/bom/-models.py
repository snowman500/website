# bom models
from extensions.models import *
from extensions.common.base_model import BaseModel



# 商品SKU模型类
class GoodsSKU(BaseModel):
    '''商品SKU模型类'''
    status_choices = (
        (0, '下线'),
        (1, '上线'),
    )

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
    status = SmallIntegerField(default=1, choices=status_choices, verbose_name='商品状态')
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

    class Meta:
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
