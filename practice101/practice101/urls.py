# /Users/yusufbagwan/Desktop/Practice/practice101/practice101/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),  # <- must be a string, not a module
]
