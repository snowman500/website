# goods models 
from extensions.models import *
from extensions.common.base_model import BaseModel
from item.models import *
from user.models import *
from datetime import datetime

# Create your models here.

class ShopChannelGroup(BaseModel):
    """商品频道组"""
    name = CharField(max_length=20, verbose_name='频道组名') # 直下式,侧入式

    class Meta:
        db_table = 'shop_channel_group'
        verbose_name = '商品频道组'
 



class ShopChannel(BaseModel):
    """商品频道"""
#    group = ForeignKey(GoodsChannelGroup, on_delete=CASCADE, verbose_name='频道组名')
    category = ForeignKey(ItemCategory, on_delete=CASCADE, verbose_name='顶级商品类别', related_name='shop_channel')
    url = CharField(max_length=50, verbose_name='频道页面链接')
    sequence = IntegerField(verbose_name='组内顺序')

    class Meta:
        db_table = 'shop_channel'
        verbose_name = '商品频道'




class ShopBrand(BaseModel):
    """品牌"""
    name = CharField(max_length=20, verbose_name='名称')
    logo = ImageField(verbose_name='Logo图片')
    first_letter = CharField(max_length=1, verbose_name='品牌首字母')

    class Meta:
        db_table = 'shop_brand'
        verbose_name = '品牌'






class ShopSPU(BaseModel):

    """商品SPU"""
    goods = CharField(max_length=10, verbose_name='物料型号:JF-D-002')  # 
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='单价')                 # 右侧详情页需要显示的
    power = DecimalField(max_digits=10, decimal_places=2, verbose_name='功率')                 # 右侧详情页需要显示的
    warranty = IntegerField(default=0, verbose_name='保修期')           # 右侧详情页需要显示的
    apply = CharField(max_length=8, verbose_name='应用范围')           # 右侧详情页需要显示的
    emitting_color = CharField(max_length=64, verbose_name='灯光颜色')      # 右侧详情页需要显示的
    transport_package = CharField(max_length=64, verbose_name='包装方式') 
#    name = ForeignKey(max_length=50, verbose_name='产品编码:F2.2.09.30.00000')
 #   caption = CharField(max_length=100, verbose_name='副标题')
 #   category = ForeignKey(ItemCategory, on_delete=PROTECT, verbose_name='从属类别',related_name='shop_spu')
 #   cost_price = DecimalField(max_digits=10, decimal_places=2, verbose_name='成本')
    market_price = DecimalField(max_digits=10, decimal_places=2, verbose_name='市场价')
    desc_detail = CharField(max_length=16, verbose_name='详细介绍')  # 这里要用TextField
    stock = IntegerField(default=0, verbose_name='库存')
    sales = IntegerField(default=0, verbose_name='销量')
    likes = IntegerField(default=0, verbose_name='收藏')
    default_image_url = ImageField(max_length=200, default='', null=True, blank=True, verbose_name='默认图片')

    class Meta:
        db_table = 'shop_spu'
        verbose_name = '商品SPU'
    def __str__(self):
        return '%s - %s' % (self.type.name, self.sku.name)

class ShopImageInfo(BaseModel):
    """图片信息表"""
    sku = ForeignKey(ItemSKU, on_delete=CASCADE, verbose_name='商品', related_name='shop_image_info')  # 其实是存的sku的id
    image_desc = CharField(max_length=100, verbose_name='图片描述')
    image = ImageField(upload_to='goods', verbose_name='主图路径')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='shop_image_info')
    image_son1 = ImageField(verbose_name='产品辅图路径1')
    image_son2 = ImageField(verbose_name='产品辅图路径2')
    image_son3 = ImageField(verbose_name='产品辅图路径3')
    image_son4 = ImageField(verbose_name='产品辅图路径4')
    image_son5 = ImageField(verbose_name='产品辅图路径5')
    image_son6 = ImageField(verbose_name='产品辅图路径6')
    image_son7 = ImageField(verbose_name='产品辅图路径7')
    image_son8 = ImageField(verbose_name='产品辅图路径8')
    image_son9 = ImageField(verbose_name='产品辅图路径9')


    class Meta:
        db_table = 'shop_image_info'
        verbose_name = '图片信息表'




class OrderMaster(BaseModel):
    """订单主表"""
    order_sn = CharField(max_length=20, unique=True, editable=False, verbose_name='订单编号') # 订单编号可以自己生成且格式为YYYYMMDDnnnnn
    customer_id = ForeignKey(CustomerInfo, on_delete=CASCADE, verbose_name='下单人ID', related_name='order_master')  # 其实是存的用户登陆的id
    shipping_user = CharField(max_length=20, unique=True, editable=False, verbose_name='订单编号')
    country = CharField(max_length=50, default='', verbose_name='国家')  #这里的默认信息从客户账户那里拿到
    province = CharField(max_length=50, default='', verbose_name='州')   #这里的默认信息从客户账户那里拿到
    city = CharField(max_length=50, default='', verbose_name='城市')     #这里的默认信息从客户账户那里拿到
    district = CharField(max_length=50, default='', verbose_name='区')   #这里的默认信息从客户账户那里拿到
    address = CharField(max_length=200, default='', verbose_name='详细地址')  #这里的默认信息从客户账户那里拿到
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
    shipping_comp_name = CharField(max_length=200, default='', verbose_name='快递公司名称')
    create_time = DateTimeField(auto_now_add=True, verbose_name='下单时间')
    shipping_time = DateTimeField(auto_now_add=True, verbose_name='发货时间')
    payment_time = DateTimeField(auto_now_add=True, verbose_name='发货时间')
    receive_time = DateTimeField(auto_now_add=True, verbose_name='收货时间')
    order_point = CharField(max_length=200, default='', verbose_name='订单积分')
    
    
    class Meta:
        db_table = 'order_master'
        verbose_name = '订单主表'


    
    
class OrderDetail(BaseModel):
    """订单详情表"""
    order_id = IntegerField( verbose_name='订单表ID')
    product_id = ForeignKey(ItemSKU, on_delete=CASCADE, verbose_name='下单人ID', related_name='order_detail')
    product_name = ForeignKey(CustomerInfo, on_delete=CASCADE, verbose_name='下单人ID', related_name='order_detail')
    product_cnt = IntegerField(default=0, verbose_name='购买商品数量')
    product_price = ForeignKey(ShopSPU, on_delete=CASCADE, verbose_name='商品价格', related_name='order_detail')
    weight = CharField(max_length=200, default='', verbose_name='商品重量')
    fee_money = CharField(max_length=200, default='', verbose_name='优惠分摊金额')
    w_id = CharField(max_length=200, default='', verbose_name='仓库ID')
    modified_time = CharField(max_length=200, default='', verbose_name='订单积分')

    class Meta:
        db_table = 'order_detail'
        verbose_name = '订单详情表'





class OrderCart(BaseModel):
    """购物车表"""
    order_id = IntegerField( verbose_name='订单表ID')
    customer_id = ForeignKey(CustomerInfo, on_delete=CASCADE, verbose_name='用户ID', related_name='order_cart')  # 其实是存的用户登陆的id
    product_id = ForeignKey(ItemSKU, on_delete=CASCADE, verbose_name='物料编码', related_name='order_cart')
    product_amount = IntegerField( verbose_name='加入购物车的数量')
    product_price = ForeignKey(ShopSPU, on_delete=CASCADE, verbose_name='商品价格', related_name='order_cart')
    create_time = DateTimeField(auto_now_add=True, verbose_name='加入购物车时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')

    
    class Meta:
        db_table = 'order_cart'
        verbose_name = '购物车表'




class ShopComment(BaseModel):
    """商品评论表"""
    is_active = BooleanField(default=True, verbose_name='激活状态') # 默认激活
    item_id = ForeignKey(ItemSKU, on_delete=CASCADE, verbose_name='商品ID', related_name='shop_comment')  # 物料编码ID
    order_id = ForeignKey(OrderMaster, on_delete=CASCADE, verbose_name='订单iD', related_name='shop_comment')  # 订单的id
    customer_id = ForeignKey(CustomerLogin, on_delete=CASCADE, verbose_name='用户登陆ID', related_name='shop_comment')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='shop_comment')
    title = CharField(max_length=100, verbose_name='评论标题')
    content = CharField(max_length=300, verbose_name='评论内容')
    audit_status = BooleanField(default=False, verbose_name='审核状态') # 默认未审核
    audit_time = DateTimeField(auto_now_add=True, verbose_name='评论创建时间')
    audit_update_time = DateTimeField(auto_now=True, verbose_name='评论修改时间')

    class Meta:
        db_table = 'shop_comment'
        verbose_name = '商品评论表'

