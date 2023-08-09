from django.urls import path

from catalog.views import shop_home, shop_contacts

urlpatterns = [
    path('', shop_home),
    path('contacts/', shop_contacts)
]