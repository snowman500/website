from django.shortcuts import render, redirect,reverse
from shop.models import *
from django.core.paginator import Paginator, Page
from django.conf import settings
from django.views.generic import View



def shop(request):
    # 获取所有ShopSPU对象
    spus = ShopSKU.objects.all()
    # 创建一个分页器对象，每页显示settings.PAGE_SIZE(这个数据是在setting中设置的)条数据
    paginator = Paginator(spus, settings.PAGE_SIZE)
    # 获取当前页码数
    page_number = request.GET.get('num')
    # 获取当前页的数据对象
    page_obj = paginator.get_page(page_number)
    # 渲染模板并返回响应
    return render(request, 'shop.html', {'page_obj': page_obj})

def single(request):
    num = request.GET.get('num')
    sku = ShopSKU.objects.filter(id=num).first
    return render(request, 'single.html',  {'sku': sku})

