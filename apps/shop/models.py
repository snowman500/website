# goods models 
from extensions.models import *
from extensions.common.base_model import BaseModel
from django.shortcuts import get_object_or_404
from user.models import *
import os

# Create your models here.


class ShopChannelGroup(BaseModel):
    """商品频道组"""
    group_name = CharField(max_length=64, verbose_name="频道组名字") 
    
    class Meta:
        db_table = 'shop_channel_group'
        verbose_name = '商品频道组'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.group_name


class ShopChannel(BaseModel):
    """商品频道"""
    channel_name = CharField(max_length=64, verbose_name="频道名字") 
    url = CharField(max_length=50, verbose_name='频道页面链接')
    sequence = IntegerField(verbose_name='组内顺序')

    class Meta:
        db_table = 'shop_channel'
        verbose_name = '商品频道'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.channel_name




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



class ShopSKU(BaseModel):
    """商品SKU"""
    goods_name = CharField(max_length=64, verbose_name='物料型号:(JF-D-***)') 
    listing = TextField(verbose_name='listing')  # 这里要用TextField
    fa_star = DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],verbose_name='评论星星')
    likes_num = IntegerField(default=0, verbose_name='收藏')
    comments = IntegerField(default=0, verbose_name='评论')
    brand = ManyToManyField(ShopBrand,  verbose_name="品牌")  # SKU--brand 多对多外键
    item_sku =  CharField(max_length=16, verbose_name='物料编码(F2.2.09.30.00000)')  
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='单价') 
    warranty = IntegerField(default=0, verbose_name='保修期')          
    transport_package = CharField(max_length=64, verbose_name='运输包装')     
    color = CharField(max_length=64, verbose_name='灯光颜色')    
    cost = DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='成本')
    likes = IntegerField(default=0, verbose_name='收藏')
    stock = IntegerField(default=0, verbose_name='库存')
    sales = IntegerField(default=0, verbose_name='销量')
    comment_num = IntegerField(default=0, verbose_name='评论数量')
    POWER_CHOICES = [
            ('1', '1W'),
            ('2', '2W'),
            ('3', '3W'),
    ]
    led_power = CharField(max_length=2, choices=POWER_CHOICES)
    PCB_MATERIAL_CHIOCES = [
            ('1', 'FR4'),
            ('2', 'Aluminum'),
    ]
    pcb_material = CharField(max_length=2, choices=PCB_MATERIAL_CHIOCES)
    pcb_w = DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, verbose_name='PCB宽度')  
    pcb_t = DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, verbose_name='PCB厚度')  
    a_pcb_l = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='A板PCB长度')          
    b_pcb_l = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='B板PCB长度')      
    c_pcb_l = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='C板PCB长度')    
    d_pcb_l = DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, verbose_name='D板PCB长度')       
    a_pcb_num = DecimalField(max_digits=2, decimal_places=0, verbose_name='一套几条A板')    
    b_pcb_num = DecimalField(max_digits=2, decimal_places=0, null=True, blank=True, verbose_name='一套几条B板')    
    c_pcb_num = DecimalField(max_digits=2, decimal_places=0, null=True, blank=True, verbose_name='一套几条C板')    
    d_pcb_num = DecimalField(max_digits=2, decimal_places=0, null=True, blank=True, verbose_name='一套几条D板')      
    led_num = CharField(max_length=8, verbose_name='LED灯珠数量')      
    lens = CharField(max_length=16, verbose_name='透镜类型')
    a_cnt = CharField(max_length=16, verbose_name='连接器1')    
    b_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='连接器2')    
    c_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='连接器3')    
    d_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='连接器4')    
    voltage = CharField(max_length=8, null=True, blank=True, verbose_name='LED灯珠电压') 
    current = DecimalField(max_digits=6, decimal_places=2, verbose_name='LED灯珠电流')     
    o_code1 = CharField(max_length=200, verbose_name='原厂代码1')   
    o_code2 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码2')  
    o_code3 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码3')  
    o_code4 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码4')  
    o_code5 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码5')  
    o_code6 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码6')  
    o_code7 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码7')  
    o_code8 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码8')  
    o_code9 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码9')  
    o_code10 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码10')  
    o_code11 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码11')  
    o_code12 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码12')  
    o_code13 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码13')  
    o_code14 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码14')  
    o_code15 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码15')  
    o_code16 = CharField(max_length=200, null=True, blank=True, verbose_name='原厂代码16')
    tv_model = TextField(null=True, blank=True,verbose_name='适用电视机型号')
    #image1 = ForeignKey(ImageField, on_delete=PROTECT,verbose_name='产品图片', related_name='sku_image')
    image1 = ImageField(upload_to='product/', verbose_name='主图')
    image2 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
    image3 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
    image4 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
    image5 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
    image6 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
    image7 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
    image8 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
    image9 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
    image10 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')

    class Meta:
        db_table = 'shop_sku'
        verbose_name = '商品SKU'
        verbose_name_plural = verbose_name

# class ShopSKUImage(BaseModel):
#     """产品图片"""
#     image1 = ImageField(upload_to='product/', verbose_name='主图')
#     image2 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
#     image3 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
#     image4 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
#     image5 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
#     image6 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
#     image7 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
#     image8 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
#     image9 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
#     image10 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
#     class Meta:
#         db_table = 'shop_sku_image'
#         verbose_name = '产品图片'
#         verbose_name_plural = verbose_name


class OrderMaster(BaseModel):
    """订单主表"""
    order_sn = CharField(max_length=20, unique=True, editable=False, verbose_name='订单编号') # 订单编号可以自己生成且格式为YYYYMMDDnnnnn
    customer_id = ForeignKey(CustomerInfo, on_delete=PROTECT, verbose_name='下单人ID', related_name='order_master')  # 其实是存的用户登陆的id
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
    customer_id = ForeignKey(CustomerInfo, on_delete=PROTECT, verbose_name='用户ID', related_name='order_cart')  # 其实是存的用户登陆的id
    product_id = ForeignKey(ItemSKU, on_delete=PROTECT, verbose_name='物料编码', related_name='order_cart')
    product_amount = IntegerField( verbose_name='加入购物车的数量')
    product_price = ForeignKey(ShopSKU, on_delete=PROTECT, verbose_name='商品价格', related_name='order_cart')


    
    class Meta:
        db_table = 'order_cart'
        verbose_name = '购物车表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.order_id



class ShopComment(BaseModel):
    """商品评论表"""
    item_id = ForeignKey(ShopSKU, on_delete=PROTECT, verbose_name='商品ID', related_name='shop_comment')  # 物料编码ID
    order_id = ForeignKey(OrderMaster, on_delete=PROTECT, verbose_name='订单iD', related_name='shop_comment')  # 订单的id
    customer_id = ForeignKey(CustomerLogin, on_delete=PROTECT, verbose_name='用户登陆ID', related_name='shop_comment')
    fa_star = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='评论星星')
    title = CharField(max_length=100, verbose_name='评论标题')
    content = CharField(max_length=300, verbose_name='评论内容')

    class Meta:
        db_table = 'shop_comment'
        verbose_name = '商品评论表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.item_id

