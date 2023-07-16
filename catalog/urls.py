from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catalog'


urlpatterns = [
    path('', cache_page(60)(views.ProductsListView.as_view()), name='product_list'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_page'),
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<slug:slug>/update/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<slug:slug>/update/', views.BlogDeleteView.as_view(), name='blog_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

