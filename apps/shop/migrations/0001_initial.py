# Generated by Django 4.2.6 on 2023-10-24 14:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(blank=True, default=True, null=True, verbose_name='启用状态')),
                ('order_sn', models.CharField(editable=False, max_length=20, unique=True, verbose_name='订单编号')),
                ('shipping_user', models.CharField(editable=False, max_length=20, unique=True, verbose_name='订单编号')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='国家')),
                ('province', models.CharField(blank=True, max_length=50, null=True, verbose_name='州')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='城市')),
                ('district', models.CharField(blank=True, max_length=50, null=True, verbose_name='区')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='详细地址')),
                ('order_money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='订单金额')),
                ('district_money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='优惠金额')),
                ('shipping_money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='运费金额')),
                ('payment_money', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='支付金额')),
                ('shipping_comp_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='快递公司名称')),
                ('shipping_time', models.DateTimeField(auto_now_add=True, verbose_name='发货时间')),
                ('payment_time', models.DateTimeField(auto_now_add=True, verbose_name='发货时间')),
                ('receive_time', models.DateTimeField(auto_now_add=True, verbose_name='收货时间')),
                ('order_point', models.CharField(blank=True, max_length=200, null=True, verbose_name='订单积分')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_master', to='user.customerinfo', verbose_name='下单人ID')),
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
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(blank=True, default=True, null=True, verbose_name='启用状态')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='品牌名称')),
                ('logo', models.ImageField(blank=True, max_length=200, null=True, upload_to='logo/', verbose_name='LOGO图片')),
                ('first_letter', models.CharField(blank=True, max_length=1, null=True, verbose_name='品牌首字母')),
                ('url', models.CharField(blank=True, max_length=50, null=True, verbose_name='品牌页面链接')),
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
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(blank=True, default=True, null=True, verbose_name='启用状态')),
                ('group_name', models.CharField(max_length=64, verbose_name='频道组名字')),
            ],
            options={
                'verbose_name': '商品频道组',
                'verbose_name_plural': '商品频道组',
                'db_table': 'shop_channel_group',
            },
        ),
        migrations.CreateModel(
            name='ShopSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(blank=True, default=True, null=True, verbose_name='启用状态')),
                ('goods_name', models.CharField(max_length=200, verbose_name='物料型号:(JF-D-***)')),
                ('item_sku', models.CharField(max_length=16, verbose_name='物料编码(F2.2.09.30.00000)')),
                ('listing', models.TextField(verbose_name='listing')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='售价')),
                ('transport_package', models.CharField(blank=True, max_length=64, null=True, verbose_name='运输包装')),
                ('likes_num', models.IntegerField(blank=True, default=0, null=True, verbose_name='收藏')),
                ('stock', models.IntegerField(blank=True, default=0, null=True, verbose_name='库存')),
                ('sales', models.IntegerField(blank=True, default=0, null=True, verbose_name='销量')),
                ('comment_num', models.IntegerField(blank=True, default=0, null=True, verbose_name='评论数量')),
                ('fa_star', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)], verbose_name='评论星星')),
                ('led_power', models.CharField(blank=True, max_length=2, null=True, verbose_name='LED灯珠瓦数')),
                ('led_type', models.CharField(blank=True, max_length=8, null=True, verbose_name='LED灯珠类型')),
                ('color', models.CharField(blank=True, max_length=2, null=True, verbose_name='灯珠发光颜色')),
                ('led_num', models.CharField(blank=True, max_length=8, null=True, verbose_name='LED灯珠数量')),
                ('voltage', models.CharField(blank=True, max_length=8, null=True, verbose_name='LED灯珠电压')),
                ('current', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='LED灯珠电流')),
                ('lens', models.CharField(blank=True, max_length=16, null=True, verbose_name='透镜类型')),
                ('pcb_material', models.CharField(blank=True, max_length=2, null=True, verbose_name='PCB板材')),
                ('pcb_w', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='PCB宽度')),
                ('pcb_t', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True, verbose_name='PCB厚度')),
                ('a_pcb', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='A/L1板名称')),
                ('a_led_num', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='A板灯珠数量')),
                ('a_pcb_num', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='A板数量')),
                ('a_pcb_l', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='A/L1板PCB长度')),
                ('aa_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='A板连接器型号A数量')),
                ('aa_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='A板连接器型号A')),
                ('ab_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='A板连接器型号B数量')),
                ('ab_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='A板连接器型号B')),
                ('ac_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='A板连接器型号C数量')),
                ('ac_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='A板连接器型号C')),
                ('b_pcb', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='B/R2板名称')),
                ('b_led_num', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='B板灯珠数量')),
                ('b_pcb_num', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True, verbose_name='B板数量')),
                ('b_pcb_l', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='B/R2板PCB长度')),
                ('ba_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='B板连接器型号A数量')),
                ('ba_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='B板连接器型号A')),
                ('bb_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='B板连接器型号B数量')),
                ('bb_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='B板连接器型号B')),
                ('bc_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='B板连接器型号C数量')),
                ('bc_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='B板连接器型号C')),
                ('c_pcb', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='C/L2板名称')),
                ('c_led_num', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='C板灯珠数量')),
                ('c_pcb_num', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True, verbose_name='C板数量')),
                ('c_pcb_l', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='C/L2板PCB长度')),
                ('ca_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='C板连接器型号A数量')),
                ('ca_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='C板连接器型号A')),
                ('cb_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='C板连接器型号B数量')),
                ('cb_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='C板连接器型号B')),
                ('cc_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='C板连接器型号C数量')),
                ('cc_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='C板连接器型号C')),
                ('d_pcb', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='D/R2板名称')),
                ('d_led_num', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='D板灯珠数量')),
                ('d_pcb_num', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True, verbose_name='D板数量')),
                ('d_pcb_l', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='D/R2板PCB长度')),
                ('da_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='D板连接器型号A数量')),
                ('da_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='D板连接器型号A')),
                ('db_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='D板连接器型号B数量')),
                ('db_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='D板连接器型号B')),
                ('dc_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='D板连接器型号C数量')),
                ('dc_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='D板连接器型号C')),
                ('e_pcb', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='E板名称')),
                ('e_led_num', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='E板灯珠数量')),
                ('e_pcb_num', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True, verbose_name='E板数量')),
                ('e_pcb_l', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='E板PCB长度')),
                ('ea_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='E板连接器型号A数量')),
                ('ea_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='E板连接器型号A')),
                ('eb_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='E板连接器型号B数量')),
                ('eb_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='E板连接器型号B')),
                ('ec_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='E板连接器型号C数量')),
                ('ec_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='E板连接器型号C')),
                ('f_pcb', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='F板名称')),
                ('f_led_num', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='F板灯珠数量')),
                ('f_pcb_num', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True, verbose_name='F板数量')),
                ('f_pcb_l', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='F板PCB长度')),
                ('fa_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='F板连接器型号A数量')),
                ('fa_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='F板连接器型号A')),
                ('fb_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='F板连接器型号B数量')),
                ('fb_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='F板连接器型号B')),
                ('fc_cnt_num', models.CharField(blank=True, max_length=16, null=True, verbose_name='F板连接器型号C数量')),
                ('fc_cnt', models.CharField(blank=True, max_length=16, null=True, verbose_name='F板连接器型号C')),
                ('o_code1', models.TextField(blank=True, null=True, verbose_name='原厂代码1')),
                ('o_code2', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码2')),
                ('o_code3', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码3')),
                ('o_code4', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码4')),
                ('o_code5', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码5')),
                ('o_code6', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码6')),
                ('o_code7', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码7')),
                ('o_code8', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码8')),
                ('o_code9', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码9')),
                ('o_code10', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码10')),
                ('o_code11', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码11')),
                ('o_code12', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码12')),
                ('o_code13', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码13')),
                ('o_code14', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码14')),
                ('o_code15', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码15')),
                ('o_code16', models.CharField(blank=True, max_length=200, null=True, verbose_name='原厂代码16')),
                ('tv_model', models.TextField(blank=True, null=True, verbose_name='适用电视机型号')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='主图')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='辅图')),
                ('brand', models.ManyToManyField(blank=True, null=True, to='shop.shopbrand', verbose_name='品牌')),
            ],
            options={
                'verbose_name': '商品SKU',
                'verbose_name_plural': '商品SKU',
                'db_table': 'shop_sku',
            },
        ),
        migrations.CreateModel(
            name='ShopComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(blank=True, default=True, null=True, verbose_name='启用状态')),
                ('fa_star', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='评论星星')),
                ('title', models.CharField(max_length=100, verbose_name='评论标题')),
                ('content', models.CharField(max_length=300, verbose_name='评论内容')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shop_comment', to='user.customerlogin', verbose_name='用户登陆ID')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shop_comment', to='shop.shopsku', verbose_name='商品ID')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shop_comment', to='shop.ordermaster', verbose_name='订单iD')),
            ],
            options={
                'verbose_name': '商品评论表',
                'verbose_name_plural': '商品评论表',
                'db_table': 'shop_comment',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(blank=True, default=True, null=True, verbose_name='启用状态')),
                ('order_id', models.IntegerField(verbose_name='订单表ID')),
                ('product_cnt', models.IntegerField(default=0, verbose_name='购买商品数量')),
                ('weight', models.CharField(blank=True, max_length=200, null=True, verbose_name='商品重量')),
                ('fee_money', models.CharField(blank=True, max_length=200, null=True, verbose_name='优惠分摊金额')),
                ('w_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='仓库ID')),
                ('modified_time', models.CharField(blank=True, max_length=200, null=True, verbose_name='订单积分')),
                ('order_sn', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderdetail_ordermaster', to='shop.ordermaster')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderdetail_itemsku', to='item.itemsku', verbose_name='下单人ID')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderdetail_customerinfo', to='user.customerinfo', verbose_name='下单人ID')),
                ('product_price', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderdetail_shopsku', to='shop.shopsku', verbose_name='商品价格')),
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
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('is_activate', models.BooleanField(blank=True, default=True, null=True, verbose_name='启用状态')),
                ('order_id', models.IntegerField(verbose_name='订单表ID')),
                ('product_amount', models.IntegerField(verbose_name='加入购物车的数量')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_cart', to='user.customerinfo', verbose_name='用户ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_cart', to='item.itemsku', verbose_name='物料编码')),
                ('product_price', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_cart', to='shop.shopsku', verbose_name='商品价格')),
            ],
            options={
                'verbose_name': '购物车表',
                'verbose_name_plural': '购物车表',
                'db_table': 'order_cart',
            },
        ),
    ]
