from django.shortcuts import render
from .models import ProductCategory, Product
from django.templatetags.static import static

# Create your views here.

def main(request):
    title = 'главная'
    products = Product.objects.all()[:4]
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)

def index(request):
    products = Product.objects.all()[:2]
    list_params = {'no': 'Vau,',
                   'p1': True,
                    'info': False
                   };

    #context = render(request, 'mainapp/index.html', context = list_params)

    context = {
        'title' : 'главная',
        'product' : 'products',
    }

    return render(request,'mainapp/index.html', context)
    #return context
    #context = render(request, 'mainapp/index.html', context=list_params)



#def main(request):
#    return render(request, 'mainapp/index.html')


def products(request):
    links_menu = [
        {'href': '', 'name': 'все'},
        {'href': '', 'name': 'дом'},
        {'href': '', 'name': 'офис'},
        {'href': '', 'name': 'модерн'},
        {'href': '', 'name': 'классика'}
    ]

    context =  {
        'title' : 'каталог',
        'links_menu' : links_menu,
        'object' : 'Product.objects.get(id = 1)'
    }


    return render(request,'mainapp/products.html',context=context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')

