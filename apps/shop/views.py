from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from django.views.generic import View
from apps.shop.models import ShopSKU, ShopChannelGroup, ShopBrand


def single(request):
    # 查询产品的所属其他属性
    num = request.GET.get('num')
    sku = ShopSKU.objects.filter(id=num).first()

    return render(request, 'single.html', {'sku': sku})


def shop(request, slug):
    """左侧边栏分栏目录循环 """
    category = get_object_or_404(ShopBrand, slug=slug)
    # 查询频道组目
    channel_group = ShopChannelGroup.objects.all()
    # 查询商品品牌
    brand = ShopBrand.objects.filter(is_activate=True)

    # 取出当前用户页码,并把这个字符转换为整型.没有娶到默认为1
    current_num = int(request.GET.get('num', 1))
    # 获取所有is_activate为ture(产品处于激活状态)的ShopSPU对象   
    skus = ShopSKU.objects.filter(is_activate=True, category=category)
    # 创建一个分页器对象，每页显示settings.PAGE_SIZE(这个数据是在setting中设置的)条数据
    paginator = Paginator(skus, settings.PAGE_SIZE)
    # 获取当前页的数据对象
    page_obj = paginator.get_page(current_num)

    # 大于11页时
    if paginator.num_pages > 11:
        # 当前页码的后5页数超过最大页码时，显示最后10项
        if current_num + 5 > paginator.num_pages:
            page_range = range(paginator.num_pages - 10, paginator.num_pages + 1)
        # 当前页码的前5页数为负数时，显示开始的10项
        elif current_num - 5 < 1:
            page_range = range(1, 12)
        else:
            # 显示左5页到右5页的页码
            page_range = range(current_num - 5, current_num + 5 + 1)
    # 小于11页时显示所有页码
    else:
        page_range = paginator.page_range

    return render(request, "shop.html",
                  {'channel_group': channel_group, 'brand': brand, "page_obj": page_obj, "paginator": paginator,
                   "current_num": current_num, "page_range": page_range})
