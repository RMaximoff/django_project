from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product


def home(request):
    data = Product.objects.all()
    return render(request, 'catalog/home.html', {'data': data})


def contact(request):
    return render(request, 'catalog/contacts.html')


def product(request, product_id):
    data = Product.objects.get(id=product_id)
    return render(request, 'catalog/product.html', {'data': data})
