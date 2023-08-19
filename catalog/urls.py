from django.urls import path

from catalog.views import shop_home, shop_contacts, discription

from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('', shop_home, name='shop_home'),
    path('contacts/', shop_contacts, name='shop_contacts'),
    path('products/', discription, name='discription'),

]