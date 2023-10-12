from django.shortcuts import render


def home(request):
    # categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    # products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    # context = {
    #     'categories': categories,
    #     'products': products,
    # }
    return render(request, 'index.html')


def about(request):
    # categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    # products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    # context = {
    #     'categories': categories,
    #     'products': products,
    # }
    return render(request, 'about.html')


def shop(request):
    # categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    # products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    # context = {
    #     'categories': categories,
    #     'products': products,
    # }
    return render(request, 'shop.html')




def single(request):
    # categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    # products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    # context = {
    #     'categories': categories,
    #     'products': products,
    # }
    return render(request, 'single.html')


def contact(request):
    # categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    # products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    # context = {
    #     'categories': categories,
    #     'products': products,
    # }
    return render(request, 'contact.html')


def faqs(request):
    # categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    # products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    # context = {
    #     'categories': categories,
    #     'products': products,
    # }
    return render(request, 'faqs.html')
