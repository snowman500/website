# Generated by Django 4.2.7 on 2023-11-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_customerbalancelog_source_sn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerlogin',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'man'), (2, 'woman'), (3, 'null')], null=True, verbose_name='性别'),
        ),
    ]
