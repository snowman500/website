from django.db import models
from django.contrib.auth.models import User




# 用户表
class JfUser(models.Model):
    # user_name = models.CharField(User, verbose_name="user_name", on_delete=models.CASCADE) # 用户名
    password = models.CharField(max_length=150, verbose_name="password") # 密码
    email = models.CharField(max_length=150, verbose_name="email address") # Email 地址
    activation = models.CharField(max_length=150, verbose_name="activation identification ") # 账户是否激活标志
    user_rights = models.CharField(max_length=150, verbose_name="User rights") # 用户权限   
    
    
# 地址表
class JfAddress(models.Model): 
    # attention = models.CharField(User, verbose_name="user_name") # 收件人
    address = models.CharField(max_length=150, verbose_name="Nearest Location") # 收件地址
    zip = models.CharField(max_length=150, verbose_name="City") # 收件邮编
    tel = models.CharField(max_length=150, verbose_name="State") # 收件电话
    
    
    
# 商品SPU表
class JfSPU(models.Model):
    product = models.CharField(max_length=150, verbose_name="Product Title") # SKU
    listing = models.TextField() # listing
    
# 商品SkU表
class JfSKU(models.Model):
    # spu = models.ForeignKey(JfSPU, verbose_name="user_name",on_delete=models.CASCADE) # SPU 外键
    # JfSKU = models.ForeignKey(JfSKU, verbose_name="user_name", on_delete=models.CASCADE) # SKU
    listing = models.CharField(max_length=150, verbose_name="listing") # listing
    # 以下是抄的
    # title = models.CharField(max_length=150, verbose_name="Product Title")
    # slug = models.SlugField(max_length=160, verbose_name="Product Slug")
    # sku = models.CharField(max_length=255, unique=True, verbose_name="Unique Product ID (SKU)")
    # short_description = models.TextField(verbose_name="Short Description")
    # detail_description = models.TextField(blank=True, null=True, verbose_name="Detail Description")
    # product_image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name="Product Image")
    # price = models.DecimalField(max_digits=8, decimal_places=2)
    # category = models.ForeignKey(Category, verbose_name="Product Categoy", on_delete=models.CASCADE)
    # is_active = models.BooleanField(verbose_name="Is Active?")
    # is_featured = models.BooleanField(verbose_name="Is Featured?")
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    # updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
    
    # class Meta:
    #     verbose_name_plural = 'Products'
    #     ordering = ('-created_at', )

    # def __str__(self):
    #     return self.title
    
    
    # title: 产品标题，类型为CharField，最大长度为150个字符。
    # slug: 产品别名，类型为SlugField，最大长度为160个字符。
    # sku: 唯一产品ID（SKU），类型为CharField，最大长度为255个字符。
    # short_description: 产品简短描述，类型为TextField。
    # detail_description: 产品详细描述，类型为TextField，可以为空。
    # product_image: 产品图片，类型为ImageField，可以为空。
    # price: 产品价格，类型为DecimalField，最多8位数字和2位小数。
    # category: 产品分类，类型为外键（ForeignKey），指向另一个模型类Category。
    # is_active: 是否激活，类型为布尔值（BooleanField）。
    # is_featured: 是否推荐，类型为布尔值（BooleanField）。
    # created_at: 创建时间，类型为日期时间（DateTimeField），自动设置当前时间。
    # updated_at: 更新时间，类型为日期时间（DateTimeField），自动设置当前时间。
    # 此外还定义了一个内部类Meta，用于设置模型的元数据。其中包括：

    # verbose_name_plural: 模型的复数名称，在管理界面中显示。
    # ordering: 模型的默认排序方式。
    # 最后还定义了一个方法__str__()用于返回对象的字符串表示形式。

    # 这个模型类可以用于创建数据库表，并且可以通过对象来访问和修改数据库中的数据。如果您需要更多关于Django模型类的信息，请参考123。