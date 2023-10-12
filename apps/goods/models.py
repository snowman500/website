# goods models 
from extensions.models import *
from extensions.common.base_model import BaseModel



# Create your models here.
class GoodsCategory(BaseModel):
    """商品类别"""
    name = CharField(max_length=10, verbose_name='名称')
    parent = ForeignKey('self', related_name='subs', null=True, blank=True, on_delete=CASCADE, verbose_name='父类别')

    class Meta:
        db_table = 'tb_goods_category'
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsChannelGroup(BaseModel):
    """商品频道组"""
    name = CharField(max_length=20, verbose_name='频道组名')

    class Meta:
        db_table = 'tb_channel_group'
        verbose_name = '商品频道组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsChannel(BaseModel):
    """商品频道"""
    group = ForeignKey(GoodsChannelGroup, on_delete=CASCADE, verbose_name='频道组名')
    category = ForeignKey(GoodsCategory, on_delete=CASCADE, verbose_name='顶级商品类别')
    url = CharField(max_length=50, verbose_name='频道页面链接')
    sequence = IntegerField(verbose_name='组内顺序')

    class Meta:
        db_table = 'tb_goods_channel'
        verbose_name = '商品频道'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category.name


class Brand(BaseModel):
    """品牌"""
    name = CharField(max_length=20, verbose_name='名称')
    logo = ImageField(verbose_name='Logo图片')
    first_letter = CharField(max_length=1, verbose_name='品牌首字母')

    class Meta:
        db_table = 'tb_brand'
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SPU(BaseModel):
    """商品SPU"""
    name = CharField(max_length=50, verbose_name='产品型号:JF-D-012')

    rating = DecimalField(max_digits=1, decimal_places=1, verbose_name='评分')
    comments = IntegerField(default=0, verbose_name='评价数')
    sales = IntegerField(default=0, verbose_name='销量')
    comments_detail = TextField(default='', verbose_name='评价详情')
    brand = ForeignKey(Brand, on_delete=PROTECT, verbose_name='品牌')
    Description = TextField(default='', verbose_name='产品listing')
    category1 = ForeignKey(GoodsCategory, on_delete=PROTECT, related_name='cat1_spu', verbose_name='一级类别')
    category2 = ForeignKey(GoodsCategory, on_delete=PROTECT, related_name='cat2_spu', verbose_name='二级类别')
    category3 = ForeignKey(GoodsCategory, on_delete=PROTECT, related_name='cat3_spu', verbose_name='三级类别')
    desc_detail = TextField(default='', verbose_name='详细介绍')
    desc_pack = TextField(default='', verbose_name='包装信息')
    # desc_service = TextField(default='', verbose_name='售后服务')

    class Meta:
        db_table = 'tb_spu'
        verbose_name = '商品SPU'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SKU(BaseModel):
    """商品SKU"""
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='单价')

    name = CharField(max_length=50, verbose_name='产品编码:F2.2.09.30.00000')
    caption = CharField(max_length=100, verbose_name='副标题')
    spu = ForeignKey(SPU, on_delete=CASCADE, verbose_name='商品')
    category = ForeignKey(GoodsCategory, on_delete=PROTECT, verbose_name='从属类别')
    cost_price = DecimalField(max_digits=10, decimal_places=2, verbose_name='成本')
    market_price = DecimalField(max_digits=10, decimal_places=2, verbose_name='市场价')
    desc_detail = TextField(default='', verbose_name='详细介绍')
    stock = IntegerField(default=0, verbose_name='库存')
    sales = IntegerField(default=0, verbose_name='销量')
    is_launched = BooleanField(default=True, verbose_name='是否上架销售')
    default_image_url = ImageField(max_length=200, default='', null=True, blank=True, verbose_name='默认图片')

    class Meta:
        db_table = 'tb_sku'
        verbose_name = '商品SKU'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.id, self.name)


class SKUImage(BaseModel):
    """SKU图片"""
    sku = ForeignKey(SKU, on_delete=CASCADE, verbose_name='sku')
    image = ImageField(verbose_name='产品主图')
    image_son1 = ImageField(verbose_name='产品辅图1')
    image_son2 = ImageField(verbose_name='产品辅图2')
    image_son3 = ImageField(verbose_name='产品辅图3')
    image_son4 = ImageField(verbose_name='产品辅图4')
    image_son5 = ImageField(verbose_name='产品辅图5')
    image_son6 = ImageField(verbose_name='产品辅图6')
    image_son7 = ImageField(verbose_name='产品辅图7')
    image_son8 = ImageField(verbose_name='产品辅图8')
    image_son9 = ImageField(verbose_name='产品辅图9')


    class Meta:
        db_table = 'tb_sku_image'
        verbose_name = 'SKU图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s %s' % (self.sku.name, self.id)


class SPUSpecification(BaseModel):
    """商品SPU规格"""
    spu = ForeignKey(SPU, on_delete=CASCADE, related_name='specs', verbose_name='商品SPU')
    name = CharField(max_length=20, verbose_name='规格名称')

    class Meta:
        db_table = 'tb_spu_specification'
        verbose_name = '商品SPU规格'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.spu.name, self.name)


class SpecificationOption(BaseModel):
    """规格选项"""
    spec = ForeignKey(SPUSpecification, related_name='options', on_delete=CASCADE, verbose_name='规格')
    value = CharField(max_length=20, verbose_name='选项值')

    class Meta:
        db_table = 'tb_specification_option'
        verbose_name = '规格选项'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.spec, self.value)


class SKUSpecification(BaseModel):
    """SKU具体规格"""
    sku = ForeignKey(SKU, related_name='specs', on_delete=CASCADE, verbose_name='sku')
    spec = ForeignKey(SPUSpecification, on_delete=PROTECT, verbose_name='规格名称')
    option = ForeignKey(SpecificationOption, on_delete=PROTECT, verbose_name='规格值')

    class Meta:
        db_table = 'tb_sku_specification'
        verbose_name = 'SKU规格'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s - %s' % (self.sku, self.spec.name, self.option.value)

