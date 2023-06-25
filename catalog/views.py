from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product
from django.views import generic


class ProductsListView(generic.ListView):
    model = Product


class ContactView(generic.TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(generic.DetailView):
    model = Product

