from django.shortcuts import render
from django.http import HttpResponse
from slugify import slugify
from catalog.models import Product, Blog
from django.views import generic
from django.urls import reverse_lazy, reverse


class ProductsListView(generic.ListView):
    model = Product


class ContactView(generic.TemplateView):
    template_name = 'catalog/contacts.html'


class ProductDetailView(generic.DetailView):
    model = Product


class BlogListView(generic.ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog
    slug_url_kwarg = 'slug'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count_views += 1
        self.object.save()
        return context


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('title', 'content', 'image')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'slug': self.object.slug})


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')
