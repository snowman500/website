# Generated by Django 4.2.6 on 2023-11-03 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_customerlogin_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerlogin',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, 'man'), (2, 'woman'), (3, 'null')], verbose_name='性别'),
        ),
    ]
