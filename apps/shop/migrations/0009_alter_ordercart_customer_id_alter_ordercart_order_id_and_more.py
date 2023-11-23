# Generated by Django 4.2.6 on 2023-11-22 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_customerlogin_avatar'),
        ('item', '0001_initial'),
        ('shop', '0008_remove_shopsku_brand_shopsku_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercart',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='OrderCart_CustomerLogin', to='user.customerlogin', verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='ordercart',
            name='order_id',
            field=models.IntegerField(verbose_name='订单编号'),
        ),
        migrations.AlterField(
            model_name='ordercart',
            name='product_amount',
            field=models.PositiveIntegerField(default=1, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='ordercart',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='OrderCart_ShopSKU', to='shop.shopsku', verbose_name='物料编码'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='OrderDetail_ItemSku', to='item.itemsku', verbose_name='下单人ID'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='OrderDetail_CustomerInfo', to='user.customerlogin', verbose_name='下单人ID'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='product_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='OrderDetail_ShopSku', to='shop.shopsku', verbose_name='商品价格'),
        ),
    ]