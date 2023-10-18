# Generated by Django 4.2.6 on 2023-10-18 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(default=True, verbose_name='启用状态')),
                ('order_sn', models.CharField(editable=False, max_length=20, unique=True, verbose_name='订单编号')),
                ('shipping_user', models.CharField(editable=False, max_length=20, unique=True, verbose_name='订单编号')),
                ('country', models.CharField(default='', max_length=50, verbose_name='国家')),
                ('province', models.CharField(default='', max_length=50, verbose_name='州')),
                ('city', models.CharField(default='', max_length=50, verbose_name='城市')),
                ('district', models.CharField(default='', max_length=50, verbose_name='区')),
                ('address', models.CharField(default='', max_length=200, verbose_name='详细地址')),
                ('order_money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='订单金额')),
                ('district_money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='优惠金额')),
                ('shipping_money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='运费金额')),
                ('payment_money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='支付金额')),
                ('shipping_comp_name', models.CharField(default='', max_length=200, verbose_name='快递公司名称')),
                ('shipping_time', models.DateTimeField(auto_now_add=True, verbose_name='发货时间')),
                ('payment_time', models.DateTimeField(auto_now_add=True, verbose_name='发货时间')),
                ('receive_time', models.DateTimeField(auto_now_add=True, verbose_name='收货时间')),
                ('order_point', models.CharField(default='', max_length=200, verbose_name='订单积分')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_master', to='user.customerinfo', verbose_name='下单人ID')),
            ],
            options={
                'verbose_name': '订单主表',
                'verbose_name_plural': '订单主表',
                'db_table': 'order_master',
            },
        ),
        migrations.CreateModel(
            name='ShopBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(default=True, verbose_name='启用状态')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('logo', models.ImageField(upload_to='', verbose_name='Logo图片')),
                ('first_letter', models.CharField(max_length=1, verbose_name='品牌首字母')),
            ],
            options={
                'verbose_name': '品牌',
                'verbose_name_plural': '品牌',
                'db_table': 'shop_brand',
            },
        ),
        migrations.CreateModel(
            name='ShopChannelGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(default=True, verbose_name='启用状态')),
                ('name', models.CharField(max_length=20, verbose_name='频道组名')),
            ],
            options={
                'verbose_name': '商品频道组',
                'verbose_name_plural': '商品频道组',
                'db_table': 'shop_channel_group',
            },
        ),
        migrations.CreateModel(
            name='ShopSPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(default=True, verbose_name='启用状态')),
                ('goods_name', models.CharField(max_length=64, verbose_name='物料型号:(JF-D-***)')),
                ('listing', models.TextField(verbose_name='listing')),
                ('warranty', models.IntegerField(default=0, verbose_name='保修期')),
                ('application', models.CharField(max_length=8, verbose_name='应用范围')),
                ('Emitting_Color', models.CharField(max_length=64, verbose_name='灯光颜色')),
                ('transport_package', models.CharField(max_length=64, verbose_name='包装方式')),
                ('sales_num', models.IntegerField(default=0, verbose_name='销量')),
                ('likes_num', models.IntegerField(default=0, verbose_name='收藏')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='shop.shopbrand')),
            ],
            options={
                'verbose_name': '商品SPU',
                'verbose_name_plural': '商品SPU',
                'db_table': 'shop_spu',
            },
        ),
        migrations.CreateModel(
            name='ShopSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(default=True, verbose_name='启用状态')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('power', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='功率')),
                ('warranty', models.IntegerField(default=0, verbose_name='保修期')),
                ('apply', models.CharField(max_length=8, verbose_name='应用范围')),
                ('color', models.CharField(max_length=64, verbose_name='灯光颜色')),
                ('transport_package', models.CharField(max_length=64, verbose_name='包装方式')),
                ('original_code', models.TextField(verbose_name='原厂代码')),
                ('stock', models.IntegerField(default=0, verbose_name='库存')),
                ('sales', models.IntegerField(default=0, verbose_name='销量')),
                ('tv_model', models.TextField(verbose_name='适用电视机型号')),
                ('likes', models.IntegerField(default=0, verbose_name='收藏')),
                ('default_image_url', models.ImageField(blank=True, default='', max_length=200, null=True, upload_to='product/', verbose_name='默认图片')),
                ('image_son1', models.ImageField(upload_to='', verbose_name='产品辅图路径1')),
                ('image_son2', models.ImageField(upload_to='', verbose_name='产品辅图路径2')),
                ('image_son3', models.ImageField(upload_to='', verbose_name='产品辅图路径3')),
                ('image_son4', models.ImageField(upload_to='', verbose_name='产品辅图路径4')),
                ('image_son5', models.ImageField(upload_to='', verbose_name='产品辅图路径5')),
                ('image_son6', models.ImageField(upload_to='', verbose_name='产品辅图路径6')),
                ('image_son7', models.ImageField(upload_to='', verbose_name='产品辅图路径7')),
                ('image_son8', models.ImageField(upload_to='', verbose_name='产品辅图路径8')),
                ('image_son9', models.ImageField(upload_to='', verbose_name='产品辅图路径9')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopspu_shopbrand', to='shop.shopbrand')),
                ('goods_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spusku', to='shop.shopspu')),
            ],
            options={
                'verbose_name': '商品SPU',
                'verbose_name_plural': '商品SPU',
                'db_table': 'shop_sku',
            },
        ),
        migrations.CreateModel(
            name='ShopComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(default=True, verbose_name='启用状态')),
                ('is_active', models.BooleanField(default=True, verbose_name='激活状态')),
                ('title', models.CharField(max_length=100, verbose_name='评论标题')),
                ('content', models.CharField(max_length=300, verbose_name='评论内容')),
                ('audit_status', models.BooleanField(default=False, verbose_name='审核状态')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_comment', to='user.customerlogin', verbose_name='用户登陆ID')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_comment', to='item.itemsku', verbose_name='商品ID')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_comment', to='shop.ordermaster', verbose_name='订单iD')),
            ],
            options={
                'verbose_name': '商品评论表',
                'verbose_name_plural': '商品评论表',
                'db_table': 'shop_comment',
            },
        ),
        migrations.CreateModel(
            name='ShopChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(default=True, verbose_name='启用状态')),
                ('url', models.CharField(max_length=50, verbose_name='频道页面链接')),
                ('sequence', models.IntegerField(verbose_name='组内顺序')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_channel', to='item.itemcategory', verbose_name='顶级商品类别')),
            ],
            options={
                'verbose_name': '商品频道',
                'verbose_name_plural': '商品频道',
                'db_table': 'shop_channel',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(default=True, verbose_name='启用状态')),
                ('order_id', models.IntegerField(verbose_name='订单表ID')),
                ('product_cnt', models.IntegerField(default=0, verbose_name='购买商品数量')),
                ('weight', models.CharField(default='', max_length=200, verbose_name='商品重量')),
                ('fee_money', models.CharField(default='', max_length=200, verbose_name='优惠分摊金额')),
                ('w_id', models.CharField(default='', max_length=200, verbose_name='仓库ID')),
                ('modified_time', models.CharField(default='', max_length=200, verbose_name='订单积分')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='item.itemsku', verbose_name='下单人ID')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='user.customerinfo', verbose_name='下单人ID')),
                ('product_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='shop.shopspu', verbose_name='商品价格')),
            ],
            options={
                'verbose_name': '订单详情表',
                'verbose_name_plural': '订单详情表',
                'db_table': 'order_detail',
            },
        ),
        migrations.CreateModel(
            name='OrderCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(default=True, verbose_name='启用状态')),
                ('order_id', models.IntegerField(verbose_name='订单表ID')),
                ('product_amount', models.IntegerField(verbose_name='加入购物车的数量')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cart', to='user.customerinfo', verbose_name='用户ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cart', to='item.itemsku', verbose_name='物料编码')),
                ('product_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_cart', to='shop.shopspu', verbose_name='商品价格')),
            ],
            options={
                'verbose_name': '购物车表',
                'verbose_name_plural': '购物车表',
                'db_table': 'order_cart',
            },
        ),
    ]
