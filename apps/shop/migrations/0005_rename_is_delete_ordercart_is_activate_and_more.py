# Generated by Django 4.2.6 on 2023-10-15 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_ordercart_is_delete_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordercart',
            old_name='is_delete',
            new_name='is_activate',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='is_delete',
            new_name='is_activate',
        ),
        migrations.RenameField(
            model_name='ordermaster',
            old_name='is_delete',
            new_name='is_activate',
        ),
        migrations.RenameField(
            model_name='shopbrand',
            old_name='is_delete',
            new_name='is_activate',
        ),
        migrations.RenameField(
            model_name='shopchannel',
            old_name='is_delete',
            new_name='is_activate',
        ),
        migrations.RenameField(
            model_name='shopchannelgroup',
            old_name='is_delete',
            new_name='is_activate',
        ),
        migrations.RenameField(
            model_name='shopcomment',
            old_name='is_delete',
            new_name='is_activate',
        ),
        migrations.RenameField(
            model_name='shopimageinfo',
            old_name='is_delete',
            new_name='is_activate',
        ),
        migrations.RenameField(
            model_name='shopspu',
            old_name='is_delete',
            new_name='is_activate',
        ),
    ]