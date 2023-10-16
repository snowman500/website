from django.shortcuts import render
from shop.models import *


# def shop(request):
#     # categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
#     # products = Product.objects.filter(is_active=True, is_featured=True)[:8]
#     # context = {
#     #     'categories': categories,
#     #     'products': products,
#     # }
#     return render(request, 'shop.html')


def single(request):
    # categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    # products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    # context = {
    #     'categories': categories,
    #     'products': products,
    # }
    return render(request, 'single.html')


def shop(request):
    # 1.0 获取数据库中所有的信息
    shop = ShopSPU.objects.all()
    
    return render(request, "shop.html", {"shop":shop})
