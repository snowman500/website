# Generated by Django 4.2.6 on 2023-10-16 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_rename_is_delete_userinfo_is_activate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='is_activate',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='update_time',
        ),
    ]
