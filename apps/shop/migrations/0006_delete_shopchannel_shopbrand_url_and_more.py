# Generated by Django 4.2.6 on 2023-10-23 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_shopsku_brand'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShopChannel',
        ),
        migrations.AddField(
            model_name='shopbrand',
            name='url',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='品牌页面链接'),
        ),
        migrations.AlterField(
            model_name='shopbrand',
            name='first_letter',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='品牌首字母'),
        ),
        migrations.AlterField(
            model_name='shopbrand',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='品牌名称'),
        ),
    ]