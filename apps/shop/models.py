# goods models 
from extensions.models import *
from extensions.common.base_model import BaseModel
from item.models import *
from user.models import *


# Create your models here.

class GoodsChannelGroup(BaseModel):
    """商品频道组"""
    name = CharField(max_length=20, verbose_name='频道组名') # 直下式,侧入式

    class Meta:
        db_table = 'shop_channel_group'
        verbose_name = '商品频道组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsChannel(BaseModel):
    """商品频道"""
#    group = ForeignKey(GoodsChannelGroup, on_delete=CASCADE, verbose_name='频道组名')
    category = ForeignKey(ItemCategory, on_delete=CASCADE, verbose_name='顶级商品类别')
    url = CharField(max_length=50, verbose_name='频道页面链接')
    sequence = IntegerField(verbose_name='组内顺序')

    class Meta:
        db_table = 'shop_channel'
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
        db_table = 'shop_brand'
        verbose_name = '品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




class SPU(BaseModel):

    """商品SPU"""
    is_launched = BooleanField(default=True, verbose_name='是否上架销售')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='单价')                 # 右侧详情页需要显示的
    power = DecimalField(max_digits=10, decimal_places=2, verbose_name='功率')                 # 右侧详情页需要显示的
    warranty = DecimalField(max_digits=10, decimal_places=2, verbose_name='保修期')             # 右侧详情页需要显示的
    warranty = DecimalField(max_digits=10, decimal_places=2, verbose_name='应用范围')           # 右侧详情页需要显示的
    emitting_color = DecimalField(max_digits=10, decimal_places=2, verbose_name='灯光颜色')     # 右侧详情页需要显示的
    transport_package = DecimalField(max_digits=10, decimal_places=2, verbose_name='包装方式')


    name = CharField(max_length=50, verbose_name='产品编码:F2.2.09.30.00000')
    caption = CharField(max_length=100, verbose_name='副标题')
 #   spu = ForeignKey(SPU, on_delete=CASCADE, verbose_name='商品')
    category = ForeignKey(ItemCategory, on_delete=PROTECT, verbose_name='从属类别')
    cost_price = DecimalField(max_digits=10, decimal_places=2, verbose_name='成本')
    market_price = DecimalField(max_digits=10, decimal_places=2, verbose_name='市场价')
    desc_detail = TextField(default='', verbose_name='详细介绍')
    stock = IntegerField(default=0, verbose_name='库存')
    sales = IntegerField(default=0, verbose_name='销量')
    likes = IntegerField(default=0, verbose_name='收藏')
    default_image_url = ImageField(max_length=200, default='', null=True, blank=True, verbose_name='默认图片')

    class Meta:
        db_table = 'shop_spu'
        verbose_name = '商品SPU'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.id, self.name)
    

class ImageInfo(BaseModel):
    """图片信息表"""
    is_active = BooleanField(default=True, verbose_name='激活状态') # 默认激活
    sku = ForeignKey('ItemSKU', on_delete=CASCADE, verbose_name='商品')  # 其实是存的sku的id
    image_desc = CharField(max_length=100, verbose_name='图片描述')
    image = ImageField(upload_to='goods', verbose_name='主图路径')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='item_image')
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
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s %s' % (self.sku.name, self.id)
    

class GoodsComment(BaseModel):
    """商品评论表"""
    is_active = BooleanField(default=True, verbose_name='激活状态') # 默认激活
    item_id = ForeignKey('SPU', on_delete=CASCADE, verbose_name='商品')  # 其实是存的spu的id
    order_id = ForeignKey('order_master', on_delete=CASCADE, verbose_name='商品')  # 订单的id
    customer_id = ForeignKey('CustomerInfo', on_delete=CASCADE, verbose_name='商品')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='item_image')
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
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s %s' % (self.sku.name, self.id)


商品评论表（product_comment）
CREATE TABLE product_comment(
  comment_id INT UNSIGNED AUTO_INCREMENT NOT NULL COMMENT '评论ID',
  product_id INT UNSIGNED NOT NULL COMMENT '商品ID',
  order_id BIGINT UNSIGNED NOT NULL COMMENT '订单ID',
  customer_id INT UNSIGNED NOT NULL COMMENT '用户ID',
  title VARCHAR(50) NOT NULL COMMENT '评论标题',
  content VARCHAR(300) NOT NULL COMMENT '评论内容',
  audit_status TINYINT NOT NULL COMMENT '审核状态：0未审核，1已审核',
  audit_time TIMESTAMP NOT NULL COMMENT '评论时间',
  modified_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后修改时间',
  PRIMARY KEY pk_commentid(comment_id)
) ENGINE = innodb COMMENT '商品评论表';


class OrderMaster(BaseModel):
    """订单主表"""
    order_sn = DecimalField(max_digits=10, decimal_places=2, verbose_name='订单编号')
    customer_id = ForeignKey('SPU', on_delete=CASCADE, verbose_name='商品')  # 其实是存的spu的id
    is_active = BooleanField(default=True, verbose_name='激活状态') # 默认激活
    order_sn = ForeignKey('SPU', on_delete=CASCADE, verbose_name='商品')  # 其实是存的spu的id


    class Meta:
        db_table = 'shop_image_info'
        verbose_name = '图片信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s %s' % (self.sku.name, self.id)
    

订单主表（order_master）
CREATE TABLE order_master(
  order_id INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '订单ID',
  order_sn BIGINT UNSIGNED NOT NULL COMMENT '订单编号 yyyymmddnnnnnnnn',
  customer_id INT UNSIGNED NOT NULL COMMENT '下单人ID',
  shipping_user VARCHAR(10) NOT NULL COMMENT '收货人姓名',
  province SMALLINT NOT NULL COMMENT '省',
  city SMALLINT NOT NULL COMMENT '市',
  district SMALLINT NOT NULL COMMENT '区',
  address VARCHAR(100) NOT NULL COMMENT '地址',
  payment_method TINYINT NOT NULL COMMENT '支付方式：1现金，2余额，3网银，4支付宝，5微信',
  order_money DECIMAL(8,2) NOT NULL COMMENT '订单金额',
  district_money DECIMAL(8,2) NOT NULL DEFAULT 0.00 COMMENT '优惠金额',
  shipping_money DECIMAL(8,2) NOT NULL DEFAULT 0.00 COMMENT '运费金额',
  payment_money DECIMAL(8,2) NOT NULL DEFAULT 0.00 COMMENT '支付金额',
  shipping_comp_name VARCHAR(10) COMMENT '快递公司名称',
  shipping_sn VARCHAR(50) COMMENT '快递单号',
  create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '下单时间',
  shipping_time DATETIME COMMENT '发货时间',
  pay_time DATETIME COMMENT '支付时间',
  receive_time DATETIME COMMENT '收货时间',
  order_status TINYINT NOT NULL DEFAULT 0 COMMENT '订单状态',
  order_point INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '订单积分',
  invoice_time VARCHAR(100) COMMENT '发票抬头',
  modified_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后修改时间',
  PRIMARY KEY pk_orderid(order_id)
)ENGINE = innodb COMMENT '订单主表';

订单详情表（order_detail）
CREATE TABLE order_detail(
  order_detail_id INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '订单详情表ID',
  order_id INT UNSIGNED NOT NULL COMMENT '订单表ID',
  product_id INT UNSIGNED NOT NULL COMMENT '订单商品ID',
  product_name VARCHAR(50) NOT NULL COMMENT '商品名称',
  product_cnt INT NOT NULL DEFAULT 1 COMMENT '购买商品数量',
  product_price DECIMAL(8,2) NOT NULL COMMENT '购买商品单价',
  average_cost DECIMAL(8,2) NOT NULL COMMENT '平均成本价格',
  weight FLOAT COMMENT '商品重量',
  fee_money DECIMAL(8,2) NOT NULL DEFAULT 0.00 COMMENT '优惠分摊金额',
  w_id INT UNSIGNED NOT NULL COMMENT '仓库ID',
    modified_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后修改时间',
  PRIMARY KEY pk_orderdetailid(order_detail_id)
)ENGINE = innodb COMMENT '订单详情表'

购物车表（order_cart）
CREATE TABLE order_cart(
  cart_id INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '购物车ID',
  customer_id INT UNSIGNED NOT NULL COMMENT '用户ID',
  product_id INT UNSIGNED NOT NULL COMMENT '商品ID',
  product_amount INT NOT NULL COMMENT '加入购物车商品数量',
  price DECIMAL(8,2) NOT NULL COMMENT '商品价格',
  add_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '加入购物车时间',
      modified_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后修改时间',
  PRIMARY KEY pk_cartid(cart_id)
) ENGINE = innodb COMMENT '购物车表';
    
