# Generated by Django 4.2.6 on 2023-10-15 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseinfo',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='启用状态'),
        ),
    ]