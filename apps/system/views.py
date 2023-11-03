from django.shortcuts import render
from apps.user.models import CustomerLogin



def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def faqs(request):
    return render(request, 'faqs.html')


def base(request):
    info_dict = request.session.get('info')
    user = CustomerLogin.objects.filter(id=info_dict.id).first()
    return render(request, 'base.html', {'user': user})
