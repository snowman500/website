# goods models 
from content.extensions.models import *
from content.extensions.common.base_model import BaseModel
from apps.user.models import *
from apps.item.models import *
from django.utils import timezone


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


class ShopBrand(BaseModel):
    """商品品牌"""
    name = CharField(max_length=20, null=True, blank=True, unique=True, verbose_name='品牌名称')
    slug = SlugField(max_length=55, verbose_name="品牌 Slug")
    logo = ImageField(max_length=200, upload_to="logo/", null=True, blank=True, verbose_name='LOGO图片')
    first_letter = CharField(max_length=1, null=True, blank=True, verbose_name='品牌首字母')
    url = CharField(max_length=50, null=True, blank=True, verbose_name='品牌页面链接')

    class Meta:
        db_table = 'shop_brand'
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ShopSKU(BaseModel):
    """商品SKU"""
    goods_name = CharField(max_length=200, verbose_name='物料型号:(JF-D-***)')
    item_sku = CharField(max_length=64, verbose_name='物料编码(F2.2.09.30.00000)')
    listing = TextField(verbose_name='listing')
    brand = ForeignKey(ShopBrand, on_delete=PROTECT, verbose_name='商品品牌',
                       related_name='sku_brand')
    price = DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='售价')
    transport_package = CharField(max_length=64, null=True, blank=True, verbose_name='运输包装')
    likes_num = IntegerField(default=0, null=True, blank=True, verbose_name='收藏')
    stock = IntegerField(default=0, null=True, blank=True, verbose_name='库存')
    sales = IntegerField(default=0, null=True, blank=True, verbose_name='销量')
    comment_num = IntegerField(default=0, null=True, blank=True, verbose_name='评论数量')
    fa_star = DecimalField(max_digits=16, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
                           null=True, blank=True, verbose_name='评论星星')
    led_power = CharField(max_length=16, null=True, blank=True, verbose_name='LED灯珠瓦数')
    led_type = CharField(max_length=16, null=True, blank=True, verbose_name='LED灯珠类型')
    color = CharField(max_length=16, null=True, blank=True, verbose_name='灯珠发光颜色')
    led_num = CharField(max_length=16, null=True, blank=True, verbose_name='LED灯珠数量')
    voltage = CharField(max_length=16, null=True, blank=True, verbose_name='LED灯珠电压')
    current = DecimalField(max_digits=16, null=True, blank=True, decimal_places=2, verbose_name='LED灯珠电流')
    lens = CharField(max_length=32, null=True, blank=True, verbose_name='透镜类型')
    pcb_material = CharField(max_length=16, null=True, blank=True, verbose_name='PCB板材')
    pcb_w = DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, verbose_name='PCB宽度')
    pcb_t = DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, verbose_name='PCB厚度')

    a_pcb = CharField(max_length=16, null=True, blank=True, verbose_name='A/L1板名称')
    a_led_num = DecimalField(max_digits=16, decimal_places=0, null=True, blank=True, verbose_name='A板灯珠数量')
    a_pcb_num = DecimalField(max_digits=16, decimal_places=0, null=True, blank=True, verbose_name='A板数量')
    a_pcb_l = DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, verbose_name='A/L1板PCB长度')
    aa_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='A板连接器型号A数量')
    aa_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='A板连接器型号A')
    ab_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='A板连接器型号B数量')
    ab_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='A板连接器型号B')
    ac_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='A板连接器型号C数量')
    ac_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='A板连接器型号C')

    b_pcb = CharField(max_length=16, null=True, blank=True, verbose_name='B/R2板名称')
    b_led_num = DecimalField(max_digits=16, decimal_places=0, null=True, blank=True, verbose_name='B板灯珠数量')
    b_pcb_num = DecimalField(max_digits=16, decimal_places=0, null=True, blank=True, verbose_name='B板数量')
    b_pcb_l = DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, verbose_name='B/R2板PCB长度')
    ba_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='B板连接器型号A数量')
    ba_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='B板连接器型号A')
    bb_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='B板连接器型号B数量')
    bb_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='B板连接器型号B')
    bc_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='B板连接器型号C数量')
    bc_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='B板连接器型号C')

    c_pcb = CharField(max_length=16, null=True, blank=True, verbose_name='C/L2板名称')
    c_led_num = DecimalField(max_digits=16, decimal_places=0, null=True, blank=True, verbose_name='C板灯珠数量')
    c_pcb_num = DecimalField(max_digits=16, decimal_places=0, null=True, blank=True, verbose_name='C板数量')
    c_pcb_l = DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, verbose_name='C/L2板PCB长度')
    ca_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='C板连接器型号A数量')
    ca_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='C板连接器型号A')
    cb_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='C板连接器型号B数量')
    cb_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='C板连接器型号B')
    cc_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='C板连接器型号C数量')
    cc_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='C板连接器型号C')

    d_pcb = CharField(max_length=16, null=True, blank=True, verbose_name='D/R2板名称')
    d_led_num = DecimalField(max_digits=16, decimal_places=0, null=True, blank=True, verbose_name='D板灯珠数量')
    d_pcb_num = DecimalField(max_digits=16, decimal_places=0, null=True, blank=True, verbose_name='D板数量')
    d_pcb_l = DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, verbose_name='D/R2板PCB长度')
    da_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='D板连接器型号A数量')
    da_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='D板连接器型号A')
    db_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='D板连接器型号B数量')
    db_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='D板连接器型号B')
    dc_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='D板连接器型号C数量')
    dc_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='D板连接器型号C')

    e_pcb = CharField(max_length=16, null=True, blank=True, verbose_name='E板名称')
    e_led_num = DecimalField(max_digits=16, decimal_places=0, null=True, blank=True, verbose_name='E板灯珠数量')
    e_pcb_num = DecimalField(max_digits=16, decimal_places=0, null=True, blank=True, verbose_name='E板数量')
    e_pcb_l = DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, verbose_name='E板PCB长度')
    ea_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='E板连接器型号A数量')
    ea_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='E板连接器型号A')
    eb_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='E板连接器型号B数量')
    eb_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='E板连接器型号B')
    ec_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='E板连接器型号C数量')
    ec_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='E板连接器型号C')

    f_pcb = CharField(max_length=16, null=True, blank=True, verbose_name='F板名称')
    f_led_num = DecimalField(max_digits=16, decimal_places=0, null=True, blank=True, verbose_name='F板灯珠数量')
    f_pcb_num = DecimalField(max_digits=16, decimal_places=0, null=True, blank=True, verbose_name='F板数量')
    f_pcb_l = DecimalField(max_digits=16, decimal_places=2, null=True, blank=True, verbose_name='F板PCB长度')
    fa_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='F板连接器型号A数量')
    fa_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='F板连接器型号A')
    fb_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='F板连接器型号B数量')
    fb_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='F板连接器型号B')
    fc_cnt_num = CharField(max_length=16, null=True, blank=True, verbose_name='F板连接器型号C数量')
    fc_cnt = CharField(max_length=16, null=True, blank=True, verbose_name='F板连接器型号C')

    o_code1 = TextField(null=True, blank=True, verbose_name='原厂代码1')
    o_code2 = TextField(null=True, blank=True, verbose_name='原厂代码2')
    o_code3 = TextField(null=True, blank=True, verbose_name='原厂代码3')
    o_code4 = TextField(null=True, blank=True, verbose_name='原厂代码4')
    o_code5 = TextField(null=True, blank=True, verbose_name='原厂代码5')
    o_code6 = TextField(null=True, blank=True, verbose_name='原厂代码6')
    o_code7 = TextField(null=True, blank=True, verbose_name='原厂代码7')
    o_code8 = TextField(null=True, blank=True, verbose_name='原厂代码8')
    o_code9 = TextField(null=True, blank=True, verbose_name='原厂代码9')
    o_code10 = TextField(null=True, blank=True, verbose_name='原厂代码10')

    tv_model = TextField(null=True, blank=True, verbose_name='适用电视机型号')
    image1 = ImageField(upload_to='product/', null=True, blank=True, verbose_name='主图')
    image2 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
    image3 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
    image4 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
    image5 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')
    image6 = ImageField(upload_to='product/', blank=True, null=True, verbose_name='辅图')

    class Meta:
        db_table = 'shop_sku'
        verbose_name = '商品SKU'
        verbose_name_plural = verbose_name


class OrderMaster(BaseModel):
    """订单主表"""
    order_sn = CharField(max_length=20, unique=True, editable=False,
                         verbose_name='订单编号')  # 订单编号可以自己生成且格式为YYYYMMDDnnnnn
    customer_id = ForeignKey(CustomerLogin, on_delete=PROTECT, verbose_name='下单人ID',
                             related_name='order_master')  # 其实是存的用户登陆的id
    shipping_user = CharField(max_length=20, unique=True, editable=False, verbose_name='订单编号')
    country = CharField(max_length=50, null=True, blank=True, verbose_name='国家')  # 这里的默认信息从客户账户那里拿到
    province = CharField(max_length=50, null=True, blank=True, verbose_name='州')  # 这里的默认信息从客户账户那里拿到
    city = CharField(max_length=50, null=True, blank=True, verbose_name='城市')  # 这里的默认信息从客户账户那里拿到
    district = CharField(max_length=50, null=True, blank=True, verbose_name='区')  # 这里的默认信息从客户账户那里拿到
    address = CharField(max_length=200, null=True, blank=True, verbose_name='详细地址')  # 这里的默认信息从客户账户那里拿到
    payment_chioces = (
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

    """我们使用了 Django 的 timezone.now() 方法获取当前时间，然后将其格式化为 YYYYMMDD 的形式作为订单编号的前缀。
    接下来，我们从数据库中获取当天已有的订单编号，找到最大的订单编号并将其序列号加 1，以生成新的订单编号。如果当天没有订单，则序列号为 1。
    最后，我们将生成的订单编号赋值给 order_sn 字段，并调用父类的 save 方法保存对象。"""

    def save(self, *args, **kwargs):
        if not self.order_sn:
            now = timezone.now()
            prefix = now.strftime('%Y%m%d')
            latest_order = OrderMaster.objects.filter(order_sn__startswith=prefix).order_by('-order_sn').first()
            if latest_order:
                order_sn = latest_order.order_sn
                serial_number = int(order_sn[-5:]) + 1
            else:
                serial_number = 1
            self.order_sn = prefix + '{:0>5d}'.format(serial_number)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_sn


class OrderDetail(BaseModel):
    """订单详情表"""
    order_sn = ForeignKey(OrderMaster, on_delete=PROTECT, related_name='orderdetail_ordermaster')  # 其实是存的用户登陆的id
    order_id = IntegerField(verbose_name='订单表ID')
    product_id = ForeignKey(ItemSKU, on_delete=PROTECT, verbose_name='下单人ID', related_name='orderdetail_itemsku')
    product_name = ForeignKey(CustomerLogin, on_delete=PROTECT, verbose_name='下单人ID',
                              related_name='orderdetail_customerinfo')
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
    order_id = IntegerField(verbose_name='订单编号')
    customer_id = ForeignKey(CustomerLogin, on_delete=PROTECT, verbose_name='用户ID',
                             related_name='order_cart')  # 其实是存的用户登陆的id
    product_id = ForeignKey(ItemSKU, on_delete=PROTECT, verbose_name='物料编码', related_name='order_cart')
    product_amount = IntegerField(verbose_name='加入购物车的数量')

    class Meta:
        db_table = 'order_cart'
        verbose_name = '购物车表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class ShopComment(BaseModel):
    """商品评论表"""
    item_id = ForeignKey(ShopSKU, on_delete=PROTECT, verbose_name='商品ID', related_name='shop_comment')  # 物料编码ID
    order_id = ForeignKey(OrderMaster, on_delete=PROTECT, verbose_name='订单iD', related_name='shop_comment')  # 订单的id
    fa_star = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='评论星星')
    title = CharField(max_length=100, verbose_name='评论标题')
    content = CharField(max_length=300, verbose_name='评论内容')

    class Meta:
        db_table = 'shop_comment'
        verbose_name = '商品评论表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.item_id
