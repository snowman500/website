# home models
from extensions.models import *
from extensions.common.base_model import BaseModel
#--------------------------------------广告部分开始----------------------------------------------

class ContentCategory(BaseModel):
    """广告内容类别"""
    name = CharField(max_length=50, verbose_name='名称')
    key = CharField(max_length=50, verbose_name='类别键名')

    class Meta:
        db_table = 'tb_content_category'
        verbose_name = '广告内容类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Content(BaseModel):
    """广告内容"""
    category = ForeignKey(ContentCategory, on_delete=PROTECT, verbose_name='类别')
    title = CharField(max_length=100, verbose_name='标题')
    url = CharField(max_length=300, verbose_name='内容链接')
    image = ImageField(null=True, blank=True, verbose_name='图片')
    text = TextField(null=True, blank=True, verbose_name='内容')
    sequence =IntegerField(verbose_name='排序')
    status = BooleanField(default=True, verbose_name='是否展示')

    class Meta:
        db_table = 'tb_content'
        verbose_name = '广告内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category.name + ': ' + self.title

#--------------------------------------广告部分结束----------------------------------------------


