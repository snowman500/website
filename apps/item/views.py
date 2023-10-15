from django.shortcuts import render


def item(request):
    # categories = Category.objects.filter(is_active=True, is_featured=True)[:3]
    # products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    # context = {
    #     'categories': categories,
    #     'products': products,
    # }
    return render(request, 'item.html')
