from django.urls import path

from django.urls import include

import mainapp.views as mainapp

app_name = 'mainapp'


def products(request, pk=None):
    print(pk)

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:pk>/', mainapp.products, name='category'),
    path('auth/', include('authapp.urls', namespace='auth')),
]



