# Generated by Django 4.2.6 on 2023-10-15 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_itemcategory_is_delete_itemsku_is_delete_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemsku',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='itemspecification',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='shippinginfo',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='warehouseinfo',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='warehouseitem',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='itemcategory',
            name='is_delete',
            field=models.BooleanField(default=True, verbose_name='启用状态'),
        ),
        migrations.AlterField(
            model_name='itemsku',
            name='is_delete',
            field=models.BooleanField(default=True, verbose_name='启用状态'),
        ),
        migrations.AlterField(
            model_name='itemspecification',
            name='is_delete',
            field=models.BooleanField(default=True, verbose_name='启用状态'),
        ),
        migrations.AlterField(
            model_name='shippinginfo',
            name='is_delete',
            field=models.BooleanField(default=True, verbose_name='启用状态'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='is_delete',
            field=models.BooleanField(default=True, verbose_name='启用状态'),
        ),
        migrations.AlterField(
            model_name='warehouseinfo',
            name='is_delete',
            field=models.BooleanField(default=True, verbose_name='启用状态'),
        ),
        migrations.AlterField(
            model_name='warehouseitem',
            name='is_delete',
            field=models.BooleanField(default=True, verbose_name='启用状态'),
        ),
    ]
