# bom models
from extensions.models import *
from extensions.common.base_model import *
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator, MaxLengthValidator

# Create your models here.
class UserInfo(BaseModel):
    """仓库信息表"""
    
    name = CharField(max_length=50, verbose_name='名字')
    password = CharField(max_length=50, verbose_name='密码')
    age = CharField(max_length=256, verbose_name='年龄')

