# klitama/views.py
from django.shortcuts import render # type: ignore

def landing_page(request):
    return render(request, "home.html")