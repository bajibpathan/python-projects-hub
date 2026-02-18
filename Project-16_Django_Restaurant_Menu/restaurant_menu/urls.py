from django.urls import path
from restaurant_menu import views

url_patterns = [
    path('', views.MenuList.as_view(), name="home")
]