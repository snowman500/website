# bom models
from extensions.models import *
from extensions.common.base_model import *
# Create your models here.
class Team(Model):

    number = CharField(max_length=32, verbose_name='编号')
    expiry_time = DateTimeField(verbose_name='到期时间')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    user_quantity = IntegerField(default=10, verbose_name='用户数量')
    remark = CharField(max_length=256, blank=True, null=True, verbose_name='备注')
    enable_auto_stock_in = BooleanField(default=False, verbose_name='启用自动入库')
    enable_auto_stock_out = BooleanField(default=False, verbose_name='启用自动出库')