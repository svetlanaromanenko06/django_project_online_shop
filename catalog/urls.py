from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import shop_contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryListView

from catalog.apps import CatalogConfig


app_name = CatalogConfig.name



urlpatterns = [

    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', shop_contacts, name='shop_contacts'),
    path('product/<int:pk>/view/', cache_page(60)(ProductDetailView.as_view()), name='product_view'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('categories/', CategoryListView.as_view(), name='category_list'),

]



