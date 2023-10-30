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
from django.urls import path, include, re_path  # 由于使用了二级路由机制，需要添加include
from apps.system import views
#以下两条是配置媒体文件
from django.views.static import serve
from django.conf import settings



urlpatterns = [
    # 配置媒体文件路由
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # 配置子路由
    path('jf/admin/', admin.site.urls),
    path('shop/',include('shop.urls')),
    path('user/',include('user.urls')),
    path('', include('system.urls')),
]
