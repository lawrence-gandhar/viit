"""inventory urls file."""

from django.test import TestCase

# Create your tests here.
from django.urls import path,include
from inventory.views import inventory_views as views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('logout',views.logout, name='logout'),
    path('login_option/<int:user_id>/', views.login_option, name='login_option'),
]