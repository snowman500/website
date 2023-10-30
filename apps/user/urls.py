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
from django.urls import path
from user import views
from .views import register


urlpatterns = [
    path('', views.login, name='user'),
	path('register/', views.register, name='register'),
	#path('logout/', views.logout, name='logout'),
    #path('CBV/', views.logout, name='logout'),	# 调用类视图的 as_view 方法
]
#视图配置(重点)

