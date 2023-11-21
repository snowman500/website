from apps.shop.models import ShopBrand
from apps.user.models import CustomerLogin


def store_menu(request):
    categories = ShopBrand.objects.filter(is_activate=True)
    context = {
        'categories_menu': categories,
    }
    return context


def cart_menu(request):
    if request.user.is_authenticated:
        cart_items = CustomerLogin.objects.filter(login_email=request.login_email)
        context = {
            'cart_items': cart_items,
        }
    else:
        context = {}
    return context
