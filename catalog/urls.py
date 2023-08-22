from django.urls import path

from catalog.views import shop_contacts, ProductListView, ProductDetailView #discription

from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [

    #path('', shop_home, name='shop_home'),
    path('', ProductListView.as_view(), name='shop_home'),
    path('contacts/', shop_contacts, name='shop_contacts'),
    path('products/', ProductDetailView.as_view(), name='discription'),
    ##path('products/', discription, name='discription'),


]

