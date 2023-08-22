from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


#def shop_home(request):
#    return render(request, 'catalog/shop_home.html')
#def shop_contacts(request):
#    return render(request, 'catalog/shop_contacts.html')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/shop_home.html'

'''def shop_home(request):
    """Контроллер для главной страницы"""

    product_list = Product.objects.all()
    context = {'object_list': product_list,
               'title': 'Интерьерный салон Нефертити'}

    return render(request, 'catalog/shop_home.html', context=context)
'''

def shop_contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/shop_contacts.html', context=context)


'''def discription(request):

    product_list = Product.objects.all()
    context = {'object_list': product_list,
               'title': 'Каталог товаров'}

    return render(request, 'catalog/discription.html', context=context)
'''


class ProductDetailView(DetailView):
    model = Product





