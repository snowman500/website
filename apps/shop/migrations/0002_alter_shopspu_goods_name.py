# Generated by Django 4.2.6 on 2023-10-17 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopspu',
            name='goods_name',
            field=models.CharField(max_length=64, verbose_name='物料型号:(JF-D-***)'),
        ),
    ]
