from django.shortcuts import render, HttpResponse, redirect
from app01.models import *

def info_list(request):
    # 1.0 获取数据库中所有的信息
    data_list = UserInfo.objects.all()
    return render(request, "info_list.html", {"data_list":data_list})
    


def info_add(request):
    if request.method == 'GET':
        return render(request, 'info_add.html')
    
    # 获取用户提交的数据
    na = request.POST.get("na")
    pa = request.POST.get("pa")
    ag = request.POST.get("ag")
    
    # 添加到数据库
    UserInfo.objects.create(name=na, password=pa, age=ag)
    
    return HttpResponse("添加成功")
    