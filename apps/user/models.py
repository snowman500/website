from content.extensions.models import *
from content.extensions.common.base_model import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import GenericIPAddressField, EmailField
import hashlib


class CustomerLogin(BaseModel):
    """用户登陆表"""
    login_email = EmailField(max_length=50, verbose_name='Email address')
    user_name = CharField(max_length=50, verbose_name='User name')
    password = CharField(max_length=128, verbose_name='Password')
    mobile_phone = CharField(max_length=50, verbose_name='Phone Number')
    last_login_time = DateTimeField(null=True, blank=True, verbose_name="最后一次登录时间")
    gender_choices = (
        (1, 'man'),
        (2, 'woman'),
        (3, 'null'),
    )
    gender = SmallIntegerField(choices=gender_choices,null=True, blank=True, verbose_name="性别")
    user_point = DecimalField(max_digits=10, decimal_places=0, null=True, blank=True, verbose_name='用户积分')
    birthday = DateField(null=True, blank=True, verbose_name='会员生日')
    user_money = DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True,
                              verbose_name='账户余额')

    class Meta:
        db_table = 'user_customer_login'  # 定义属性表名字
        verbose_name = '用户登陆表'
        verbose_name_plural = verbose_name

    # @classmethod
    # def encrypt_password(cls, password):
    #     """使用SHA-1加密密码，返回长度为40的加密后的字符串。"""
    #     return hashlib.sha1(password.encode()).hexdigest()


class CustomerLevelInfo(BaseModel):
    """用户级别表"""
    is_active = BooleanField(default=True, verbose_name='启用状态')  #
    customer_level = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], verbose_name='会员级别ID')
    level_name = CharField(max_length=50, verbose_name='会员级别名称')
    min_point = IntegerField(verbose_name='该级别最低积分')
    max_point = IntegerField(verbose_name='该级别最高积分')
    update_time = DateTimeField(auto_now=True, verbose_name='最后修改时间')

    class Meta:
        db_table = 'user_customer_level_info'  # 定义属性表名字
        verbose_name = '用户级别表'
        verbose_name_plural = verbose_name


class CustomerAddress(BaseModel):
    """用户地址表"""
    is_default = BooleanField(default=True, verbose_name='是否默认地址')
    zip_code = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(999999)], verbose_name='邮编地址')
    level_name = CharField(max_length=50, verbose_name='会员级别名称')
    customer_name = CharField(max_length=50, verbose_name='收件人姓名')
    mobile_phone = CharField(max_length=50, verbose_name='收件人手机号码')
    country = CharField(max_length=50, verbose_name='国家')
    province = CharField(max_length=50, verbose_name='州')
    city = CharField(max_length=50, verbose_name='城市')
    district = CharField(max_length=50, verbose_name='区')
    address = CharField(max_length=200, verbose_name='详细地址')
    update_time = DateTimeField(auto_now=True, verbose_name='最后修改时间')

    class Meta:
        db_table = 'user_customer_address'  # 定义属性表名字
        verbose_name = '用户地址表'
        verbose_name_plural = verbose_name


class CustomerPointLog(BaseModel):
    """用户积分日志表"""
    level_name = CharField(max_length=50, verbose_name='会员级别名称')
    country = CharField(max_length=50, verbose_name='国家')
    province = CharField(max_length=50, verbose_name='州')
    city = CharField(max_length=50, verbose_name='城市')
    district = CharField(max_length=50, verbose_name='区')
    address = CharField(max_length=200, verbose_name='区')
    update_time = DateTimeField(auto_now=True, verbose_name='最后修改时间')
    is_default = BooleanField(default=True, verbose_name='是否默认地址')
    refer_number = IntegerField(verbose_name='积分来源编号')
    change_point = CharField(max_length=200, verbose_name='变更积分数')
    create_time = DateTimeField(auto_now_add=True, verbose_name='积分日志生成时间')

    class Meta:
        db_table = 'user_customer_point_info'  # 定义属性表名字
        verbose_name = '用户积分日志表'
        verbose_name_plural = verbose_name


class CustomerBalanceLog(BaseModel):
    """用户余额变动表"""
    source_chioces = (
        (1, 'order'),
        (2, 'rejected'),
    )
    source_sn = SmallIntegerField(choices=source_chioces, verbose_name='相关单据')
    create_time = DateTimeField(auto_now_add=True, verbose_name='记录日志生成时间')
    amount = IntegerField(verbose_name='变动金额')

    class Meta:
        db_table = 'user_customer_balance_log'  # 定义属性表名字
        verbose_name = '用户余额变动表'
        verbose_name_plural = verbose_name


class CustomerLoginLog(BaseModel):
    """用户登录日志表"""
    login_ip_address = GenericIPAddressField(null=True, blank=True, verbose_name='用户登陆IP')
    login_type = (
        ('1', 'succeed'),
        ('2', 'def'),
    )
    source_sn = SmallIntegerField(choices=login_type, verbose_name='相关单据')
    create_time = DateTimeField(auto_now_add=True, verbose_name='记录日志生成时间')
    amount = IntegerField(verbose_name='变动金额')

    class Meta:
        db_table = 'user_customer_login_log'  # 定义属性表名字
        verbose_name = '用户登录日志表'
        verbose_name_plural = verbose_name
