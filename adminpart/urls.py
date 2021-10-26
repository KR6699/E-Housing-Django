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
import django
from django.contrib import admin, auth
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.admin_login,name = 'adminpart'),
    path('add_society/', views.add_society, name = 'add_society'),
    path('add_house/', views.add_house, name = 'add_house'),
    path('house_report/', views.h_report, name = 'house_report'),
    path('house_allocate/', views.h_allocate, name = 'house_allocate'),
    path('home/', views.home,name = 'home'),
    path('member_report/', views.m_report, name = 'member_report'),
    path('society_report/', views.society_report, name = 'society_report'),
    path('admin_complain/', views.admin_complain, name = 'admin_complain'),
    path('sell_h_report/', views.sh_report, name = 'sell_h_report'),
    path('rent_h_report/', views.rh_report, name = 'rent_h_report'),
    path('delete/<int:pk>', views.delete, name = 'delete'),
    path('delete_society/<str:pk>', views.delete_society, name = 'delete_society'),
    path('delete_member/<str:pk>', views.delete_member, name = 'delete_member'),
    path('delete_sh/<int:pk>', views.delete_sh, name = 'delete_sh'),
    path('delete_rh/<int:pk>', views.delete_rh, name = 'delete_rh'),
    path('solve/<int:pk>', views.solve, name = 'solve'),
    path('logout/', views.admin_logout, name = 'logout'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)