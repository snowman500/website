from django.shortcuts import render
from shop.models import *
from django.core.paginator import Paginator, Page
from django.conf import settings

def single(request):
    return render(request, 'single.html')


# def shop(request):
#     # 1.0 获取数据库中所有的信息
#     shop = ShopSPU.objects.all()    
#     return render(request, "shop.html", {"shop":shop})


def shop(request):
    # 获取所有ShopSPU对象
    spus = ShopSPU.objects.all()
    # 创建一个分页器对象，每页显示settings.PAGE_SIZE(这个数据是在setting中设置的)条数据
    paginator = Paginator(spus, settings.PAGE_SIZE)
    # 获取当前页码数
    page_number = request.GET.get('num')
    # 获取当前页的数据对象
    page_obj = paginator.get_page(page_number)
    # 遍历当前页的ShopSPU对象，获取第一个ShopSKU对象的price属性值
    for spu in page_obj:
        sku_list = spu.spu_sku.all()
        if sku_list:
            spu.price = sku_list[0].price
            spu.image = sku_list[0].image
    # 渲染模板并返回响应
    return render(request, 'shop.html', {'page_obj': page_obj})

def single(request):
    # 获取当前查询的是第几个产品
    num = request.GET.get('num')
    # 去数据库查询对应的产品的所有属性
    sku_list = ShopSPU.objects.filter(id=num).first()
    # 把查到的属性返回给前端
    return render(request, 'single.html', {'sku_list': sku_list},)
