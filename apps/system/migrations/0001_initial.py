# Generated by Django 4.2.6 on 2023-10-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32, verbose_name='编号')),
                ('expiry_time', models.DateTimeField(verbose_name='到期时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user_quantity', models.IntegerField(default=10, verbose_name='用户数量')),
                ('remark', models.CharField(blank=True, max_length=256, null=True, verbose_name='备注')),
                ('enable_auto_stock_in', models.BooleanField(default=False, verbose_name='启用自动入库')),
                ('enable_auto_stock_out', models.BooleanField(default=False, verbose_name='启用自动出库')),
            ],
        ),
    ]
