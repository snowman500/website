# Generated by Django 4.2.6 on 2023-11-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_customerlogin_birthday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerlogin',
            name='gender',
            field=models.SmallIntegerField(choices=[('1', 'man'), ('2', 'woman'), ('3', 'null')], verbose_name='性别'),
        ),
    ]
