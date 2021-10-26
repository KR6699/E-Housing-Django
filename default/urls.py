"""ehousing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index,name = 'index'),
    # path('user_login', views.user_login,name = 'user_login'),
    path('user_logout', views.user_logout,name = 'user_logout'),
    path('my_account', views.my_account,name = 'my_account'),
    path('my_home', views.my_home,name = 'my_home'),
    path('my_msg', views.my_msg,name = 'my_msg'),
    path('complain', views.complain,name = 'complain'),
    path('rent', views.rent,name = 'rent'),
    path('sell', views.sell,name = 'sell'),
    path('selllist', views.selllist,name = 'selllist'),
    path('rentlist', views.rentlist,name = 'rentlist'),
    path('sell_house_view/<int:pk>', views.sell_h_view,name = 'sell_house_view'),
    path('rent_house_view/<int:pk>', views.rent_h_view,name = 'rent_house_view'),
    path('societylist/<int:pk>', views.societylist,name = 'societylist'),
    path('message/<str:pk>', views.message,name = 'message'),
    path('delete/<int:pk>', views.delete,name = 'delete_msg'),
]
