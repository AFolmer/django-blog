# Views for main mysite pages

from django.shortcuts import render


def home(request):
    return render(request, "home.html")
