from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.ProductsListView.as_view(), name='product_list'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_page'),
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('blog/<slug:slug>/update/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<slug:slug>/delete/', views.BlogDeleteView.as_view(), name='blog_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

