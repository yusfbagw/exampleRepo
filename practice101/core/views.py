from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def button_clicked(request):
    return HttpResponse("❤️ You clicked the heart!")
