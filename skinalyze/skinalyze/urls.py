"""
URL configuration for skinalyze project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),

    path('register/',register,name='register'),
    path('login/',user_login,name='user_login'), 
    path('winter_deep/', winter_deep, name='winter_deep'),
    path('winter_cool/', winter_cool, name='winter_cool'),
    path('winter_bright/', winter_bright, name='winter_bright'),
    path('summer_soft/', summer_soft, name='summer_soft'),
    path('summer_cool/', summer_cool, name='summer_cool'),
    path('summer_light/', summer_light, name='summer_light'),
    path('spring_warm/',spring_warm, name='spring_warm'),
    path('spring_light/', spring_light, name='spring_light'),
    path('spring_bright/', spring_bright, name='spring_bright'),
    path('autumn_deep/', autumn_deep, name='autumn_deep'),
    path('autumn_warm/', autumn_warm, name='autumn_warm'),
    path('autumn_soft/',autumn_soft, name='autumn_soft'),
]
