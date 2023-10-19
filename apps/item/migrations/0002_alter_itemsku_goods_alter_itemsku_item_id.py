# Generated by Django 4.2.6 on 2023-10-19 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsku',
            name='goods',
            field=models.CharField(max_length=64, verbose_name='物料型号(JF-D-002)'),
        ),
        migrations.AlterField(
            model_name='itemsku',
            name='item_id',
            field=models.CharField(max_length=16, verbose_name='物料编码(F2.2.09.30.00000)'),
        ),
    ]
