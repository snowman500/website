# Generated by Django 4.2.6 on 2023-10-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_alter_shopsku_led_power_alter_shopsku_pcb_material'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopchannelgroup',
            options={},
        ),
        migrations.RemoveField(
            model_name='shopchannel',
            name='category',
        ),
        migrations.RemoveField(
            model_name='shopchannelgroup',
            name='name',
        ),
        migrations.AddField(
            model_name='shopchannel',
            name='channel_name',
            field=models.CharField(default=1, max_length=64, verbose_name='频道名字'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopchannelgroup',
            name='group_name',
            field=models.CharField(default=1, max_length=64, verbose_name='频道组名字'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shopsku',
            name='pcb_material',
            field=models.CharField(choices=[('1', 'FR4'), ('2', 'Aluminum')], max_length=2),
        ),
        migrations.AlterModelTable(
            name='shopchannelgroup',
            table=None,
        ),
    ]
