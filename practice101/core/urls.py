# /Users/yusufbagwan/Desktop/Practice/practice101/core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("clicked/", views.button_clicked, name="button_clicked"),
]
