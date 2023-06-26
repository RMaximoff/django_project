from catalog.models import Product, Blog, Version
from django.views import generic
from django.urls import reverse_lazy, reverse
from catalog.forms import BlogForm, ProductForm


class ContactView(generic.TemplateView):
    template_name = 'catalog/contacts.html'


class ProductsListView(generic.ListView):
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_versions = Version.objects.filter(is_current=True).select_related('product')
        context['active_versions'] = active_versions
        return context


class ProductDetailView(generic.DetailView):
    model = Product


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save_versions(self.object)
        return response


class ProductDeleteView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')


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
    form_class = BlogForm
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class BlogUpdateView(generic.UpdateView):
    model = Blog
    form_class = BlogForm

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'slug': self.object.slug})


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')
