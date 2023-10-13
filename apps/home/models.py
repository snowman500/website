# # home models
# from extensions.models import *
# from extensions.common.base_model import BaseModel
# #--------------------------------------广告部分开始----------------------------------------------

# class ContentCategory(BaseModel):
#     """广告内容类别"""
#     name = CharField(max_length=50, verbose_name='名称')
#     key = CharField(max_length=50, verbose_name='类别键名')

#     class Meta:
#         db_table = 'tb_content_category'
#         verbose_name = '广告内容类别'
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.name

# class Content(BaseModel):
#     """广告内容"""
#     category = ForeignKey(ContentCategory, on_delete=PROTECT, verbose_name='类别')
#     title = CharField(max_length=100, verbose_name='标题')
#     url = CharField(max_length=300, verbose_name='内容链接')
#     image = ImageField(null=True, blank=True, verbose_name='图片')
#     text = TextField(null=True, blank=True, verbose_name='内容')
#     sequence =IntegerField(verbose_name='排序')
#     status = BooleanField(default=True, verbose_name='是否展示')

#     class Meta:
#         db_table = 'goods_content'
#         verbose_name = '广告内容'
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.category.name + ': ' + self.title

# #--------------------------------------广告部分结束----------------------------------------------

# # '首页轮播商品'
# class IndexGoodsBanner(BaseModel):
#     '''首页轮播商品展示模型类'''
#     sku = ForeignKey('ItemSKU.item_id', on_delete=CASCADE, verbose_name='商品')  # 其实是存的sku的id
#     image = ImageField(upload_to='banner', verbose_name='图片')
#     index = SmallIntegerField(default=0, verbose_name='展示顺序')  # 0 1 2 3

#     class Meta:
#         db_table = 'df_index_banner'
#         verbose_name = '首页轮播商品'
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.sku.name


# # "主页分类展示商品"
# class IndexTypeGoodsBanner(BaseModel):
#     '''首页分类商品展示模型类'''
#     DISPLAY_TYPE_CHOICES = (
#         (0, "标题"),
#         (1, "图片")
#     )

#     type = ForeignKey('type', on_delete=CASCADE, verbose_name='商品类型')  # 其实是存的GoodsType的id
#     sku = ForeignKey('item_id', on_delete=CASCADE, verbose_name='商品SKU')  # 其实是存的GoodsSKU的id
#     display_type = SmallIntegerField(default=1, choices=DISPLAY_TYPE_CHOICES, verbose_name='展示类型')
#     index = SmallIntegerField(default=0, verbose_name='展示顺序')

#     class Meta:
#         db_table = 'df_index_type_goods'
#         verbose_name = "主页分类展示商品"
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return '%s - %s' % (self.type.name, self.sku.name)


# # "主页促销活动"
# class IndexPromotionBanner(BaseModel):
#     '''首页促销活动模型类'''
#     name = CharField(max_length=20, verbose_name='活动名称')
#     url = CharField(max_length=256, verbose_name='活动链接')
#     image = ImageField(upload_to='banner', verbose_name='活动图片')  # 去调用FastDfs存储图片
#     index = SmallIntegerField(default=0, verbose_name='展示顺序')

#     class Meta:
#         db_table = 'df_index_promotion'
#         verbose_name = "主页促销活动"
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.name