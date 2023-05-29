from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'catalog/home.html')


def contact(request):
    return render(request, 'catalog/contacts.html')