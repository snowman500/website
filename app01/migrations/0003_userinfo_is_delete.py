# Generated by Django 4.2.6 on 2023-10-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_remove_userinfo_is_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='删除标记'),
        ),
    ]
