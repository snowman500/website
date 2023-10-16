from django.shortcuts import render, HttpResponse, redirect
from item.models import *

def item_list(request):
    # 1.0 获取数据库中所有的信息
    item_list = WarehouseInfo.objects.all()
    
    return render(request, "item_list.html", {"item_list":item_list})



def item(request):
    if request.method == 'GET':
        return render(request, 'item.html')
    
    # 获取用户提交的数据
    warehouse_code = request.POST.get("warehouse_code")
    warehouse_name = request.POST.get("warehouse_name")
    link_man = request.POST.get("link_man")
    phone_number = request.POST.get("phone_number")
    province = request.POST.get("province")
    city = request.POST.get("city")
    distrct = request.POST.get("distrct")
    address = request.POST.get("address")
    
    # 添加到数据库
    WarehouseInfo.objects.create(warehouse_code=warehouse_code,
                                warehouse_name=warehouse_name,
                                link_man=link_man,
                                phone_number=phone_number,
                                province=province,
                                city=city,
                                distrct=distrct,
                                address=address)
    
    return HttpResponse("添加成功")


def delete(request):
    nid = request.GET.get("nid")
    WarehouseInfo.objects.filter(id=nid).delete()
    return redirect("/item/list/")