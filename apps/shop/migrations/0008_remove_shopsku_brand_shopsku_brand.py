# Generated by Django 4.2.6 on 2023-11-17 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_shopbrand_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopsku',
            name='brand',
        ),
        migrations.AddField(
            model_name='shopsku',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='sku_brand', to='shop.shopbrand', verbose_name='商品品牌'),
            preserve_default=False,
        ),
    ]