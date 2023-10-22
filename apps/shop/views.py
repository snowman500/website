from django.shortcuts import render, redirect,reverse
from django.core.paginator import Paginator
from django.conf import settings
from django.views.generic import View
from shop.models import ShopSKU, ShopChannel, ShopChannelGroup




def single(request):
    num = request.GET.get('num')
    sku = ShopSKU.objects.filter(id=num).first
    return render(request, 'single.html',  {'sku': sku})



def shop(request):
    """左侧边栏分栏目录循环 """
    # 查询频道组目
    channel_group = ShopChannelGroup.objects.all()
    # 查询频道类目
    channel = ShopChannel.objects.all()
    
    
    """商品列表栏商品循环 """
    # 获取所有ShopSPU对象   
    spus = ShopSKU.objects.all()
    # 创建一个分页器对象，每页显示settings.PAGE_SIZE(这个数据是在setting中设置的)条数据
    paginator = Paginator(spus, settings.PAGE_SIZE)
    # 获取当前页码数
    page_number = request.GET.get('num')
    # 获取当前页的数据对象
    page_obj = paginator.get_page(page_number)
    # 渲染模板并返回响应
    
    return render(request, 'shop.html', {'channel_group':channel_group,'channel':channel,'page_obj': page_obj})
    
    