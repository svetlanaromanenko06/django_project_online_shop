from django.urls import path

from catalog.views import shop_home, shop_contacts

from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('', shop_home),
    path('contacts/', shop_contacts),
]