from django.shortcuts import render, HttpResponse, redirect
from item.models import *


def item(request):
    # categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    # products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    # context = {
    #     'categories': categories,
    #     'products': products,
    # }
    if request.WarehouseInfo == "GET":
        return render(request, 'item.html')
    warehouse_code = request.POST.get("warehouse_code")
    warehouse_name = request.POST.get("warehouse_name")
    link_man = request.POST.get("link_man")
    phone_number = request.POST.get("phone_number")
    province = request.POST.get("province")
    city = request.POST.get("city")
    distrct = request.POST.get("distrct")
    address = request.POST.get("address")
    
    WarehouseInfo.objects.create(warehouse_code="warehouse_code",
                                 warehouse_name="warehouse_name",
                                 link_man="link_man",
                                 phone_number="phone_number",
                                 province="province",
                                 city="city",
                                 distrct="distrct",
                                 address="address",
                                 )
    return HttpResponse("添加成功")