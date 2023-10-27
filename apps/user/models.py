from extensions.models import * 
from extensions.common.base_model import BaseModel 
from item.models import * 
from django.contrib.auth.hashers import make_password 
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomerLogin(BaseModel):
    """用户登录表"""
    is_active = BooleanField(default=True, verbose_name='启用状态')     # 真上线,假下线
    login_name = CharField(max_length=50, verbose_name='用户登录名')
    password = models.CharField(max_length=128, verbose_name='用户登录密码')

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    class Meta:
        db_table = 'user_customer_login' # 定义属性表名字
        verbose_name = '用户登录表'
        verbose_name_plural = verbose_name

class CustomerInfo(BaseModel):
    """用户信息表"""
    customer_id = ForeignKey(CustomerLogin, on_delete=CASCADE, verbose_name='用户登录表ID')
    customer_name = CharField(max_length=50, verbose_name='用户真实姓名')
    identity_card_no = CharField(max_length=50, verbose_name='证件号码')    
    identity_choices = (
        ('1', '身份证'),
        ('2', '军官证'),
        ('3', '护照'),
        ('4', '驾驶证'),
        )
    mobile_phone = CharField(max_length=50, verbose_name='手机号码')   
    customer_email = CharField(max_length=50, verbose_name='用户邮箱')   
    gender_choices = (
        ('0', 'man'),
        ('1', 'woman'),
        ('2', 'null'),
        )
    gender = IntegerField(choices=gender_choices, default=2,verbose_name="性别")
    user_point = DecimalField(max_digits=10, decimal_places=0, verbose_name='用户积分')
    birthday = CharField(max_length=50, verbose_name='会员生日')   
    user_money = DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='账户余额')
    last_login_time = models.DateTimeField(null=True, blank=True,verbose_name="最后一次登录时间")

    class Meta:
        db_table = 'user_customer_info' # 定义属性表名字
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name


class CustomerLevelInfo(BaseModel):
    """用户级别表"""
    is_active = BooleanField(default=True, verbose_name='启用状态')     # 
    customer_level = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='会员级别ID')
    level_name = CharField(max_length=50, verbose_name='会员级别名称')
    min_point = IntegerField(verbose_name='该级别最低积分')
    max_point = IntegerField(verbose_name='该级别最高积分')
    password = models.CharField(max_length=128, verbose_name='用户登录密码')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')

    class Meta:
        db_table = 'user_customer_level_info' # 定义属性表名字
        verbose_name = '用户级别表'
        verbose_name_plural = verbose_name


class CustomerAddress(BaseModel):
    """用户地址表"""
    customer_id = ForeignKey(CustomerLogin, on_delete=CASCADE, verbose_name='用户登录表ID')
    zip_code = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999999)], verbose_name='邮编地址')
    level_name = CharField(max_length=50, verbose_name='会员级别名称')
    country = CharField(max_length=50, verbose_name='国家')
    province = CharField(max_length=50, verbose_name='州')
    city = CharField(max_length=50, verbose_name='城市')
    district = CharField(max_length=50, verbose_name='区')
    address = CharField(max_length=200, verbose_name='详细地址')
    password = models.CharField(max_length=128, verbose_name='用户登录密码')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')
    is_default = BooleanField(default=True, verbose_name='是否默认地址') 


    class Meta:
        db_table = 'user_customer_address' # 定义属性表名字
        verbose_name = '用户地址表'
        verbose_name_plural = verbose_name



class CustomerPointLog(BaseModel):
    """用户积分日志表"""
    customer_id = ForeignKey(CustomerLogin, on_delete=CASCADE, verbose_name='用户登录表ID')
    source_chioces = (
        ('1', 'order'),
        ('2', 'loging'),
        ('3', 'party'),
        )
    level_name = CharField(max_length=50, verbose_name='会员级别名称')
    country = CharField(max_length=50, verbose_name='国家')
    province = CharField(max_length=50, verbose_name='州')
    city = CharField(max_length=50, verbose_name='城市')
    district = CharField(max_length=50, verbose_name='区')
    address = CharField(max_length=200, verbose_name='区')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')
    is_default = BooleanField(default=True, verbose_name='是否默认地址') 
    refer_number = IntegerField( verbose_name='积分来源编号')
    change_point = CharField(max_length=200, verbose_name='变更积分数')
    create_time = DateTimeField(auto_now_add=True, verbose_name='积分日志生成时间')


    class Meta:
        db_table = 'user_customer_point_info' # 定义属性表名字
        verbose_name = '用户积分日志表'
        verbose_name_plural = verbose_name



class CustomerBalanceLog(BaseModel):
    """用户余额变动表"""
    customer_id = ForeignKey(CustomerLogin, on_delete=CASCADE, verbose_name='用户登录表ID')
    source_sn = IntegerField( verbose_name='相关单据')
    source_chioces = (
        ('1', 'order'),
        ('2', 'rejected'),
        )
    source_sn = IntegerField( verbose_name='相关单据')
    create_time = DateTimeField(auto_now_add=True, verbose_name='记录日志生成时间')
    amount = IntegerField( verbose_name='变动金额')


    class Meta:
        db_table = 'user_customer_balance_log' # 定义属性表名字
        verbose_name = '用户余额变动表'
        verbose_name_plural = verbose_name

class CustomerLoginLog(BaseModel):
    """用户登录日志表"""
    customer_id = ForeignKey(CustomerLogin, on_delete=CASCADE, verbose_name='用户登录表ID')
    create_time = DateTimeField(auto_now_add=True, verbose_name='用户登陆时间')
    login_ip_address =models.GenericIPAddressField(null=True, blank=True,  verbose_name='用户登陆IP')
    login_type = (
        ('1', 'succeed'),
        ('2', 'def'),
        )
    source_sn = IntegerField( verbose_name='相关单据')
    create_time = DateTimeField(auto_now_add=True, verbose_name='记录日志生成时间')
    amount = IntegerField( verbose_name='变动金额')


    class Meta:
        db_table = 'user_customer_login_log' # 定义属性表名字
        verbose_name = '用户登录日志表'
        verbose_name_plural = verbose_name

