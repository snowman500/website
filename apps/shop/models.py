# goods models 
from extensions.models import *
from extensions.common.base_model import BaseModel
from item.models import *
from user.models import *

# Create your models here.

class ShopChannelGroup(BaseModel):
    """商品频道组"""
    name = CharField(max_length=20, verbose_name='频道组名') # 直下式,侧入式

    class Meta:
        db_table = 'shop_channel_group'
        verbose_name = '商品频道组'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.name




class ShopChannel(BaseModel):
    """商品频道"""
#    group = ForeignKey(GoodsChannelGroup, on_delete=CASCADE, verbose_name='频道组名')
    category = ForeignKey(ItemCategory, on_delete=CASCADE, verbose_name='顶级商品类别', related_name='shop_channel')
    url = CharField(max_length=50, verbose_name='频道页面链接')
    sequence = IntegerField(verbose_name='组内顺序')

    class Meta:
        db_table = 'shop_channel'
        verbose_name = '商品频道'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.category




class ShopBrand(BaseModel):
    """品牌"""
    name = CharField(max_length=20, verbose_name='名称')
    logo = ImageField(max_length=200, upload_to="LOGO/", null=True, blank=True, verbose_name='LOGO图片')
    first_letter = CharField(max_length=1, verbose_name='品牌首字母')

    class Meta:
        db_table = 'shop_brand'
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ShopSPU(BaseModel):

    """商品SPU"""
    goods_name = CharField(max_length=64, verbose_name='物料型号:(JF-D-***)')  # 
    brand = ForeignKey(ShopBrand, on_delete=CASCADE, related_name='brand')  # 右侧详情页需要显示的
    listing = TextField(verbose_name='listing')  # 这里要用TextField
    warranty = IntegerField(default=0, verbose_name='保修期')           # 右侧详情页需要显示的
    application = CharField(max_length=8, verbose_name='应用范围')           # 右侧详情页需要显示的
    Emitting_Color = CharField(max_length=64, verbose_name='灯光颜色')      # 右侧详情页需要显示的
    transport_package = CharField(max_length=64, verbose_name='包装方式') 
    fa_star = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='评论星星')
    sales_num = IntegerField(default=0, verbose_name='销量')
    likes_num = IntegerField(default=0, verbose_name='收藏')
    

    class Meta:
        db_table = 'shop_spu'
        verbose_name = '商品SPU'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.goods_name

class ShopSKU(BaseModel):
    """商品SKU"""
    goods_name = ForeignKey(ShopSPU, on_delete=CASCADE, related_name='spusku')  # SKU--SPU
    brand = ForeignKey(ShopBrand, on_delete=CASCADE, related_name='shopspu_shopbrand')  # 品牌
    item_sku = ForeignKey(ItemSKU, on_delete=CASCADE, related_name='shopspu_itemsku')  # 产品物料编码
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='单价')   # 右侧详情页需要显示的
    warranty = IntegerField(default=0, verbose_name='保修期')           # 右侧详情页需要显示的
    apply = CharField(max_length=8, verbose_name='应用范围')           # 右侧详情页需要显示的
    color = CharField(max_length=64, verbose_name='灯光颜色')      # 右侧详情页需要显示的
    transport_package = CharField(max_length=64, verbose_name='包装方式') 
#   cost_price = DecimalField(max_digits=10, decimal_places=2, verbose_name='成本')
#   cost = DecimalField(max_digits=10, decimal_places=2, verbose_name='成本')
    original_code1 = CharField(default='', null=True, blank=True,verbose_name='原厂代码1')  
    original_code2 = CharField(verbose_name='原厂代码2')  
    original_code3 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码3')  
    original_code4 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码4')  
    original_code5 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码5')  
    original_code6 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码6')  
    original_code7 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码7')  
    original_code8 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码8')  
    original_code9 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码9')  
    original_code10 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码10')  
    original_code11 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码11')  
    original_code12 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码12')  
    original_code13 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码13')  
    original_code14 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码14')  
    original_code15 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码15')  
    original_code16 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码16')  
    stock = IntegerField(default=0, verbose_name='库存')
    sales = IntegerField(default=0, verbose_name='销量')
    tv_model = TextField(verbose_name='适用电视机型号')
    likes = IntegerField(default=0, verbose_name='收藏')
    default_image_url = ImageField(max_length=200, upload_to="product/",  null=True, blank=True, verbose_name='默认图片')
    image_son1 = ImageField(max_length=200, upload_to="product/", null=True, blank=True, verbose_name='产品辅图1')
    image_son2 = ImageField(max_length=200, upload_to="product/", null=True, blank=True, verbose_name='产品辅图2')
    image_son3 = ImageField(max_length=200, upload_to="product/", null=True, blank=True, verbose_name='产品辅图3')
    image_son4 = ImageField(max_length=200, upload_to="product/", null=True, blank=True, verbose_name='产品辅图4')
    image_son5 = ImageField(max_length=200, upload_to="product/", null=True, blank=True, verbose_name='产品辅图5')
    image_son6 = ImageField(max_length=200, upload_to="product/", null=True, blank=True, verbose_name='产品辅图6')
    image_son7 = ImageField(max_length=200, upload_to="product/", null=True, blank=True, verbose_name='产品辅图7')
    image_son8 = ImageField(max_length=200, upload_to="product/", null=True, blank=True, verbose_name='产品辅图8')
    image_son9 = ImageField(max_length=200, upload_to="product/", null=True, blank=True, verbose_name='产品辅图9')
    power_chioces= (
        ('1', '1W'),
        ('2', '2W'),
        ('3', '3W'),
        )   # 1W/2W/3W
    voltage_chioces= (
        ('1', '3V'),
        ('2', '6V'),
        )   # 3V/6V
    pcb_width= (
        ('3', '3mm'),
        ('4', '4mm'),
        ('5', '5mm'),
        ('6', '6mm'),
        ('7', '7mm'),
        ('8', '8mm'),
        ('9', '9mm'),
        ('10', '10mm'),
        ('11', '11mm'),
        ('12', '12mm'),
        ('14', '14mm'),
        ('15', '15mm'),
        ('16', '16mm'),
        ('17', '17mm'),
        ('18', '18mm'),
        ('20', '20mm'),
        ('22', '22mm'),
        )   # PCB宽度

    class Meta:
        db_table = 'shop_sku'
        verbose_name = '商品SKU'
        verbose_name_plural = verbose_name


class OrderMaster(BaseModel):
    """订单主表"""
    order_sn = CharField(max_length=20, unique=True, editable=False, verbose_name='订单编号') # 订单编号可以自己生成且格式为YYYYMMDDnnnnn
    customer_id = ForeignKey(CustomerInfo, on_delete=CASCADE, verbose_name='下单人ID', related_name='order_master')  # 其实是存的用户登陆的id
    shipping_user = CharField(max_length=20, unique=True, editable=False, verbose_name='订单编号')
    country = CharField(max_length=50, null=True, blank=True, verbose_name='国家')  #这里的默认信息从客户账户那里拿到
    province = CharField(max_length=50, null=True, blank=True, verbose_name='州')   #这里的默认信息从客户账户那里拿到
    city = CharField(max_length=50, null=True, blank=True, verbose_name='城市')     #这里的默认信息从客户账户那里拿到
    district = CharField(max_length=50, null=True, blank=True, verbose_name='区')   #这里的默认信息从客户账户那里拿到
    address = CharField(max_length=200, null=True, blank=True, verbose_name='详细地址')  #这里的默认信息从客户账户那里拿到
    payment_chioces= (
        ('1', 'paypal'),
        ('2', 'card'),
        ('3', '**'),
        ('4', 'TT'),
        )
    order_money = DecimalField(max_digits=10, decimal_places=2, verbose_name='订单金额')    
    district_money = DecimalField(max_digits=10, decimal_places=2, verbose_name='优惠金额')    
    shipping_money = DecimalField(max_digits=10, decimal_places=2, verbose_name='运费金额')    
    payment_money = DecimalField(max_digits=10, decimal_places=2, verbose_name='支付金额')    
    shipping_comp_name = CharField(max_length=200, null=True, blank=True, verbose_name='快递公司名称')
    shipping_time = DateTimeField(auto_now_add=True, verbose_name='发货时间')
    payment_time = DateTimeField(auto_now_add=True, verbose_name='发货时间')
    receive_time = DateTimeField(auto_now_add=True, verbose_name='收货时间')
    order_point = CharField(max_length=200, null=True, blank=True, verbose_name='订单积分')
    
    
    class Meta:
        db_table = 'order_master'
        verbose_name = '订单主表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.order_sn


    
    
class OrderDetail(BaseModel):
    """订单详情表"""
    order_sn = ForeignKey(OrderMaster, on_delete=PROTECT, related_name='orderdetail_ordermaster')  # 其实是存的用户登陆的id
    order_id = IntegerField( verbose_name='订单表ID')
    product_id = ForeignKey(ItemSKU, on_delete=PROTECT, verbose_name='下单人ID', related_name='orderdetail_itemsku')
    product_name = ForeignKey(CustomerInfo, on_delete=PROTECT, verbose_name='下单人ID', related_name='orderdetail_customerinfo')
    product_cnt = IntegerField(default=0, verbose_name='购买商品数量')
    product_price = ForeignKey(ShopSKU, on_delete=PROTECT, verbose_name='商品价格', related_name='orderdetail_shopsku')
    weight = CharField(max_length=200, null=True, blank=True, verbose_name='商品重量')
    fee_money = CharField(max_length=200, null=True, blank=True, verbose_name='优惠分摊金额')
    w_id = CharField(max_length=200, null=True, blank=True, verbose_name='仓库ID')
    modified_time = CharField(max_length=200, null=True, blank=True, verbose_name='订单积分')

    class Meta:
        db_table = 'order_detail'
        verbose_name = '订单详情表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.order_id





class OrderCart(BaseModel):
    """购物车表"""
    order_id = IntegerField( verbose_name='订单表ID')
    customer_id = ForeignKey(CustomerInfo, on_delete=CASCADE, verbose_name='用户ID', related_name='order_cart')  # 其实是存的用户登陆的id
    product_id = ForeignKey(ItemSKU, on_delete=CASCADE, verbose_name='物料编码', related_name='order_cart')
    product_amount = IntegerField( verbose_name='加入购物车的数量')
    product_price = ForeignKey(ShopSPU, on_delete=CASCADE, verbose_name='商品价格', related_name='order_cart')


    
    class Meta:
        db_table = 'order_cart'
        verbose_name = '购物车表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.order_id




class ShopComment(BaseModel):
    """商品评论表"""
    item_id = ForeignKey(ItemSKU, on_delete=CASCADE, verbose_name='商品ID', related_name='shop_comment')  # 物料编码ID
    order_id = ForeignKey(OrderMaster, on_delete=CASCADE, verbose_name='订单iD', related_name='shop_comment')  # 订单的id
    customer_id = ForeignKey(CustomerLogin, on_delete=CASCADE, verbose_name='用户登陆ID', related_name='shop_comment')
    fa_star = IntegerField(default=0, verbose_name='评论星星')
    title = CharField(max_length=100, verbose_name='评论标题')
    content = CharField(max_length=300, verbose_name='评论内容')

    class Meta:
        db_table = 'shop_comment'
        verbose_name = '商品评论表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.item_id

