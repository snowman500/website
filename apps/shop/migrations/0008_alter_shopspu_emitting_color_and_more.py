# Generated by Django 4.2.6 on 2023-10-16 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_shopspu_category_remove_shopspu_cost_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopspu',
            name='emitting_color',
            field=models.CharField(max_length=64, verbose_name='灯光颜色'),
        ),
        migrations.AlterField(
            model_name='shopspu',
            name='transport_package',
            field=models.CharField(max_length=64, verbose_name='包装方式'),
        ),
        migrations.AlterField(
            model_name='shopspu',
            name='warranty',
            field=models.CharField(max_length=64, verbose_name='应用范围'),
        ),
    ]