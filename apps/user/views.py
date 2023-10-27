from django.shortcuts import render


def login(request):
    # categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    # products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    # context = {
    #     'categories': categories,
    #     'products': products,
    # }
    return render(request, 'login.html')


def logout(request):
    # categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    # products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    # context = {
    #     'categories': categories,
    #     'products': products,
    # }
    return render(request, 'logout.html')


def register(request):
    # categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    # products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    # context = {
    #     'categories': categories,
    #     'products': products,
    # }
    return render(request, 'register.html')