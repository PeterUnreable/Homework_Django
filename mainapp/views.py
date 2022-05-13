from django.shortcuts import render

# Create your views here.


def index(request):
    list_params = {'no': 'Vau,',
                   'p1': True,
                    'info': False
                   };

    context = render(request, 'mainapp/index.html', context = list_params)
    return context

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
        'links_menu' : links_menu
    }


    return render(request,'mainapp/products.html',context=context)


def contacts(request):
    return render(request, 'mainapp/contacts.html')

