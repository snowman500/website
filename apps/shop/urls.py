"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.shop import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('category/<str:brand_name>/', views.category, name='category'),
    path('single/<str:goods_name>/', views.single, name="single"),
    path('cart/', views.cart, name="cart"),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
]
