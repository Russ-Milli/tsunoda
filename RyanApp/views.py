from django.shortcuts import render
from django.http import HttpResponse


def karibu(request):
    return HttpResponse("<h1>Karibu to Django</h1>")


def homepage(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'contact us.html')


def personal(request):
    return render(request, 'Personal Details.html')


def login(request):
    return render(request, 'login.html')


def services(request):
    return render(request, 'services.html')


def gallery(request):
    return render(request, 'gallery.html')
