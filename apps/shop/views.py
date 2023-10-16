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
    # 获取当前查询的是第几页
    num = request.GET.get('num')
    contact_list = ShopSPU.objects.all()
    # 创建Paginator 实例对象
    paginator = Paginator(contact_list,settings.PAGE_SIZE) # 每页显示25个联系人
    # page = request.GET.get('page')
    # 获取Page 对象
    contacts = paginator.get_page(num)
    return render(request, 'shop.html', {'contacts': contacts,})


def single(request):
    # 获取当前查询的是第几个产品
    num = request.GET.get('num')
    # 去数据库查询对应的产品的所有属性
    sku_list = ShopSPU.objects.filter(id=num).first()
    # 把查到的属性返回给前端
    return render(request, 'single.html', {'sku_list': sku_list,})


""" 下面还有点问题 """
# 生成分页数值列表[1,2,3,4,5,6,7,8,9]
# setting 中设置了几个常量
# def get_range_list(num,total_page,size=9):
#     """
#     num:当前页
#     total_page:总页数
#     size:列表个数
#     """
#     min = num - int(size/2)
#     min = min if min>=2 else 2
#     max = min + size - 2
#     max = max if max <= total_page else total_page
    
#     return range(min,max+1)




# def shop(request):
#     # 获取当前查询的是第几页
#     num = request.GET.get('num')
#     contact_list = ShopSPU.objects.all()
#     # 创建Paginator 实例对象
#     paginator = Paginator(contact_list,settings.PAGE_SIZE) # 每页显示25个联系人
#     # page = request.GET.get('page')
#     # 获取Page 对象
#     contacts = paginator.get_page(num)
#     # 生成列表
#     page_range_list = get_range_list(contacts.number, paginator.num_pages,settings.RANGE_LIST_SIZE )
#     return render(request, 'shop.html', {'contacts': contacts,'page_range_list':page_range_list})

