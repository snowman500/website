import decimal
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from apps.shop.models import ShopSKU, ShopChannelGroup, ShopBrand, OrderCart
from django.contrib.auth.decorators import login_required


def single(request, goods_name):
    # 查询产品的所属其他属性
    sku = get_object_or_404(ShopSKU, goods_name=goods_name)

    return render(request, 'single.html', {'sku': sku})


def cart(request, goods_name):
    # 查询产品的所属其他属性
    sku = get_object_or_404(ShopSKU, goods_name=goods_name)

    return render(request, 'cart.html', {'sku': sku})


#@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = get_object_or_404(ShopSKU, id=product_id)

    # Check whether the Product is already in Cart or Not
    item_already_in_cart = OrderCart.objects.filter(product=product_id, user=user)
    if item_already_in_cart:
        cp = get_object_or_404(OrderCart, product_id=product_id, customer_id=user)
        cp.product_amount += 1
        cp.save()
    else:
        OrderCart(customer_id=user, product_id=product).save()

    return redirect('store:cart')


# def cart(request):
#     user = request.user
#     cart_products = Cart.objects.filter(user=user)
#
#     # Display Total on Cart Page
#     amount = decimal.Decimal(0)
#     shipping_amount = decimal.Decimal(10)
#     # using list comprehension to calculate total amount based on quantity and shipping
#     cp = [p for p in Cart.objects.all() if p.user == user]
#     if cp:
#         for p in cp:
#             temp_amount = (p.quantity * p.product.price)
#             amount += temp_amount
#
#     # Customer Addresses
#     addresses = Address.objects.filter(user=user)
#
#     context = {
#         'cart_products': cart_products,
#         'amount': amount,
#         'shipping_amount': shipping_amount,
#         'total_amount': amount + shipping_amount,
#         'addresses': addresses,
#     }
#     return render(request, 'store/cart.html', context)
#
#
# def remove_cart(request, cart_id):
#     if request.method == 'GET':
#         c = get_object_or_404(Cart, id=cart_id)
#         c.delete()
#         messages.success(request, "Product removed from Cart.")
#     return redirect('store:cart')
#
#
# def plus_cart(request, cart_id):
#     if request.method == 'GET':
#         cp = get_object_or_404(Cart, id=cart_id)
#         cp.quantity += 1
#         cp.save()
#     return redirect('store:cart')
#
#
# def minus_cart(request, cart_id):
#     if request.method == 'GET':
#         cp = get_object_or_404(Cart, id=cart_id)
#         # Remove the Product if the quantity is already 1
#         if cp.quantity == 1:
#             cp.delete()
#         else:
#             cp.quantity -= 1
#             cp.save()
#     return redirect('store:cart')


def shop(request):
    """左侧边栏分栏目录循环 """
    # 查询频道组目
    channel_group = ShopChannelGroup.objects.all()
    # 查询商品品牌
    brands = ShopBrand.objects.filter(is_activate=True)
    # 取出当前用户页码,并把这个字符转换为整型.没有娶到默认为1
    current_num = int(request.GET.get('num', 1))
    # 获取所有is_activate为ture(产品处于激活状态)的ShopSPU对象
    skus = ShopSKU.objects.filter(is_activate=True)
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
                  {'channel_group': channel_group, 'brands': brands, "page_obj": page_obj, "paginator": paginator,
                   "current_num": current_num, "page_range": page_range})


def category(request, brand_name):
    """左侧边栏分栏目录循环 """
    # 查询频道组目
    channel_group = ShopChannelGroup.objects.all()
    # 查询商品品牌
    brands = ShopBrand.objects.filter(is_activate=True)
    # 取出当前商品品牌,没有取到到默认为lg
    brand = get_object_or_404(ShopBrand, name=brand_name)

    # brand =  ShopBrand.objects.filter(is_activate=True)
    # 获取所有is_activate为ture(产品处于激活状态)的ShopSPU对象   
    skus = ShopSKU.objects.filter(is_activate=True, brand=brand)
    # 取出当前用户页码,并把这个字符转换为整型.没有娶到默认为1
    current_num = int(request.GET.get('num', 1))
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

    return render(request, "category.html",
                  {'channel_group': channel_group, 'brand': brand, 'brands': brands, 'page_obj': page_obj,
                   'paginator': paginator,
                   'current_num': current_num, 'page_range': page_range})
