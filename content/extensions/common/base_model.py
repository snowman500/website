# coding=utf-8
from django.db import models


class BaseModel(models.Model):
    '''模型抽象基类'''
    create_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name='更新时间')
    is_activate = models.BooleanField(default=True, null=True, blank=True, verbose_name='启用状态') # 默认启用

    class Meta:
        # 说明是一个抽象模型类
        abstract = True
