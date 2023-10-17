# Generated by Django 4.2.6 on 2023-10-17 03:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerLevelInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='启用状态')),
                ('customer_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='会员级别ID')),
                ('level_name', models.CharField(max_length=50, verbose_name='会员级别名称')),
                ('min_point', models.IntegerField(verbose_name='该级别最低积分')),
                ('max_point', models.IntegerField(verbose_name='该级别最高积分')),
                ('password', models.CharField(max_length=128, verbose_name='用户登录密码')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name': '用户级别表',
                'verbose_name_plural': '用户级别表',
                'db_table': 'user_customer_level_info',
            },
        ),
        migrations.CreateModel(
            name='CustomerLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='启用状态')),
                ('login_name', models.CharField(max_length=50, verbose_name='用户登录名')),
                ('password', models.CharField(max_length=128, verbose_name='用户登录密码')),
            ],
            options={
                'verbose_name': '用户登录表',
                'verbose_name_plural': '用户登录表',
                'db_table': 'user_customer_login',
            },
        ),
        migrations.CreateModel(
            name='CustomerPointLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=50, verbose_name='会员级别名称')),
                ('country', models.CharField(max_length=50, verbose_name='国家')),
                ('province', models.CharField(max_length=50, verbose_name='州')),
                ('city', models.CharField(max_length=50, verbose_name='城市')),
                ('district', models.CharField(max_length=50, verbose_name='区')),
                ('address', models.CharField(max_length=200, verbose_name='区')),
                ('password', models.CharField(max_length=128, verbose_name='用户登录密码')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('is_default', models.BooleanField(default=True, verbose_name='是否默认地址')),
                ('refer_number', models.IntegerField(verbose_name='积分来源编号')),
                ('change_point', models.CharField(max_length=200, verbose_name='变更积分数')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='积分日志生成时间')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customerlogin', verbose_name='用户登录表ID')),
            ],
            options={
                'verbose_name': '用户积分日志表',
                'verbose_name_plural': '用户积分日志表',
                'db_table': 'user_customer_point_info',
            },
        ),
        migrations.CreateModel(
            name='CustomerLoginLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='用户登陆IP')),
                ('source_sn', models.IntegerField(verbose_name='相关单据')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='记录日志生成时间')),
                ('amount', models.IntegerField(verbose_name='变动金额')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customerlogin', verbose_name='用户登录表ID')),
            ],
            options={
                'verbose_name': '用户登录日志表',
                'verbose_name_plural': '用户登录日志表',
                'db_table': 'user_customer_login_log',
            },
        ),
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50, verbose_name='用户真实姓名')),
                ('identity_card_no', models.CharField(max_length=50, verbose_name='证件号码')),
                ('mobile_phone', models.CharField(max_length=50, verbose_name='手机号码')),
                ('customer_email', models.CharField(max_length=50, verbose_name='用户邮箱')),
                ('user_point', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='用户积分')),
                ('register_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后登录时间')),
                ('birthday', models.CharField(max_length=50, verbose_name='会员生日')),
                ('user_money', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='账户余额')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customerlogin', verbose_name='用户登录表ID')),
            ],
            options={
                'verbose_name': '用户登录表',
                'verbose_name_plural': '用户登录表',
                'db_table': 'user_customer_info',
            },
        ),
        migrations.CreateModel(
            name='CustomerBalanceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_sn', models.IntegerField(verbose_name='相关单据')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='记录日志生成时间')),
                ('amount', models.IntegerField(verbose_name='变动金额')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customerlogin', verbose_name='用户登录表ID')),
            ],
            options={
                'verbose_name': '用户积分日志表',
                'verbose_name_plural': '用户积分日志表',
                'db_table': 'user_customer_balance_log',
            },
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999999)], verbose_name='邮编地址')),
                ('level_name', models.CharField(max_length=50, verbose_name='会员级别名称')),
                ('country', models.CharField(max_length=50, verbose_name='国家')),
                ('province', models.CharField(max_length=50, verbose_name='州')),
                ('city', models.CharField(max_length=50, verbose_name='城市')),
                ('district', models.CharField(max_length=50, verbose_name='区')),
                ('address', models.CharField(max_length=200, verbose_name='详细地址')),
                ('password', models.CharField(max_length=128, verbose_name='用户登录密码')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('is_default', models.BooleanField(default=True, verbose_name='是否默认地址')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customerlogin', verbose_name='用户登录表ID')),
            ],
            options={
                'verbose_name': '用户地址表',
                'verbose_name_plural': '用户地址表',
                'db_table': 'user_customer_address',
            },
        ),
    ]
