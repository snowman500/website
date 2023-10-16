# Generated by Django 4.2.6 on 2023-10-15 02:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('item_id', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)], verbose_name='物料分类代码')),
                ('item', models.CharField(max_length=10, verbose_name='物料名称')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_category', to='item.itemcategory', verbose_name='父类别')),
            ],
            options={
                'verbose_name': '物料类别',
                'verbose_name_plural': '物料类别',
                'db_table': 'item_item_category',
            },
        ),
        migrations.CreateModel(
            name='ItemUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('remark', models.CharField(blank=True, max_length=256, null=True, verbose_name='备注')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('is_active', models.BooleanField(default=False, verbose_name='启用状态')),
                ('supplier_code', models.CharField(default='JF0000', max_length=10, verbose_name='启用状态')),
                ('supplier_name', models.CharField(max_length=50, verbose_name='供应商名称')),
                ('link_man', models.CharField(max_length=256, verbose_name='联系人')),
                ('phone_number', models.CharField(max_length=50, verbose_name='联系人电话')),
                ('bank_name', models.CharField(max_length=50, verbose_name='供应商开户银行名称')),
                ('bank_account', models.CharField(max_length=50, verbose_name='银行账号')),
                ('address', models.CharField(max_length=50, verbose_name='供应商地址')),
            ],
            options={
                'verbose_name': '供应商信息表',
                'verbose_name_plural': '供应商信息表',
                'db_table': 'item_supplier',
            },
        ),
        migrations.CreateModel(
            name='WarehouseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('is_active', models.BooleanField(default=False, verbose_name='启用状态')),
                ('warehouse_code', models.CharField(max_length=50, verbose_name='仓库编码')),
                ('warehouse_name', models.CharField(max_length=50, verbose_name='仓库名称')),
                ('link_man', models.CharField(max_length=256, verbose_name='仓库联系人')),
                ('phone_number', models.CharField(max_length=50, verbose_name='仓库联系人电话')),
                ('province', models.CharField(max_length=50, verbose_name='省')),
                ('city', models.CharField(max_length=50, verbose_name='市')),
                ('distrct', models.CharField(max_length=50, verbose_name='区')),
                ('address', models.CharField(max_length=50, verbose_name='仓库地址')),
            ],
            options={
                'verbose_name': '仓库信息表',
                'verbose_name_plural': '仓库信息表',
                'db_table': 'item_warehouse_info',
            },
        ),
        migrations.CreateModel(
            name='WarehouseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('is_active', models.BooleanField(default=True, verbose_name='启用状态')),
                ('product_id', models.CharField(max_length=50, verbose_name='物料ID')),
                ('current_cnt', models.CharField(max_length=256, verbose_name='库存数量')),
                ('lock_cnt', models.CharField(max_length=50, verbose_name='锁库数量')),
                ('in_transit_cnt', models.CharField(max_length=50, verbose_name='在途数量')),
                ('w_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='warehouse_item', to='item.warehouseinfo', verbose_name='仓库ID')),
            ],
            options={
                'verbose_name': '物料库存表',
                'verbose_name_plural': '物料库存表',
                'db_table': 'item_warehouse_item',
            },
        ),
        migrations.CreateModel(
            name='ShippingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('is_active', models.BooleanField(default=True, verbose_name='启用状态')),
                ('ship_name', models.CharField(max_length=50, verbose_name='物流公司名称')),
                ('link_man', models.CharField(max_length=256, verbose_name='物流公司联系人')),
                ('phone_number', models.CharField(max_length=50, verbose_name='物流公司联系人电话')),
                ('price', models.CharField(max_length=50, verbose_name='价格')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_info', to='system.team')),
            ],
            options={
                'verbose_name': '物流公司信息表',
                'verbose_name_plural': '物流公司信息表',
                'db_table': 'item_ShippingInfo',
            },
        ),
        migrations.CreateModel(
            name='ItemSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('is_active', models.BooleanField(default=True, verbose_name='激活状态')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='物料价格')),
                ('product_specification', models.BooleanField(default=False, verbose_name='规格书是否已经上传')),
                ('remark', models.CharField(blank=True, max_length=256, null=True, verbose_name='备注')),
                ('spec_1', models.CharField(max_length=64, verbose_name='自定义规格1')),
                ('spec_2', models.CharField(max_length=64, verbose_name='自定义规格2')),
                ('spec_3', models.CharField(max_length=64, verbose_name='自定义规格3')),
                ('spec_4', models.CharField(max_length=64, verbose_name='自定义规格4')),
                ('spec_5', models.CharField(max_length=64, verbose_name='自定义规格5')),
                ('spec_6', models.CharField(max_length=64, verbose_name='自定义规格6')),
                ('spec_7', models.CharField(max_length=64, verbose_name='自定义规格7')),
                ('spec_8', models.CharField(max_length=64, verbose_name='自定义规格8')),
                ('spec_9', models.CharField(max_length=64, verbose_name='自定义规格9')),
                ('spec_10', models.CharField(max_length=64, verbose_name='自定义规格10')),
                ('spec_11', models.CharField(max_length=64, verbose_name='自定义规格11')),
                ('spec_12', models.CharField(max_length=64, verbose_name='自定义规格12')),
                ('spec_13', models.CharField(max_length=64, verbose_name='自定义规格13')),
                ('spec_14', models.CharField(max_length=64, verbose_name='自定义规格14')),
                ('spec_15', models.CharField(max_length=64, verbose_name='自定义规格15')),
                ('spec_16', models.CharField(max_length=64, verbose_name='自定义规格16')),
                ('spec_17', models.CharField(max_length=64, verbose_name='自定义规格17')),
                ('spec_18', models.CharField(max_length=64, verbose_name='自定义规格18')),
                ('spec_19', models.CharField(max_length=64, verbose_name='自定义规格19')),
                ('spec_20', models.CharField(max_length=64, verbose_name='自定义规格20')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item_specification', to='item.supplier', verbose_name='供应商名称')),
            ],
            options={
                'verbose_name': '物料属性表',
                'verbose_name_plural': '物料属性表',
                'db_table': 'item_item_specification',
            },
        ),
        migrations.CreateModel(
            name='ItemSKU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('is_active', models.BooleanField(default=True, verbose_name='激活状态')),
                ('is_launched', models.BooleanField(default=True, verbose_name='是否上架销售')),
                ('goods', models.CharField(max_length=64, verbose_name='物料型号:JF-D-002')),
                ('item_id', models.CharField(max_length=20, verbose_name='物料编码:F2.2.09.30.00000')),
                ('name', models.CharField(max_length=20, verbose_name='物料名称')),
                ('desc', models.CharField(max_length=256, verbose_name='物料简介')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='物料价格')),
                ('unite', models.CharField(max_length=20, verbose_name='物料单位')),
                ('image', models.ImageField(upload_to='goods', verbose_name='物料图片')),
                ('stock', models.IntegerField(default=1, verbose_name='物料库存')),
                ('sales', models.IntegerField(default=0, verbose_name='物料销量')),
                ('brand', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='灯条品牌')),
                ('set', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='一套几条')),
                ('enable_inventory_warning', models.BooleanField(default=False, verbose_name='启用库存警告')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_sku', to='item.itemcategory', verbose_name='物料类型编码')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]