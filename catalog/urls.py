from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.ProductsListView.as_view(), name='product_list'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

