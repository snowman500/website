"""
URL configuration for officeshop project.

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
from django.urls import path, include
from apps.user import views

urlpatterns = [
    path('login/', views.login, name='user'),  # 指向views视图文件的视图函数
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name='logout'),
    path('image/code/', views.image_code, name='check_code'),

]
