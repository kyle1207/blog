"""cnblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from django.views.static import serve

from blog import views
from cnblog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('get_validCode_img/', views.get_validCode_img),
    path('index/', views.index),
    # 根地址即显示主页内容
    re_path('^$', views.index),
    path('register/', views.register),
    path('logout/', views.logout),



    # media 配置
    re_path(r"media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT})
]
