from django.urls import path
from AppTienda.views import *

urlpatterns = [
    path('', inicio),
    path('producto/', producto),
    path('cliente/', cliente),
    path('vendedor/', vendedor),
    path('entrega/', entrega),
]


def inicio(request):
    return HttpResponse('Pagina de inicio')

def producto(request):
    return HttpResponse('Pagina de productos')

def cliente(request):
    return HttpResponse('Pagina de clientes')

def vendedor(request):
    return HttpResponse('Pagina de vendedores')

def entrega(request):
    return HttpResponse('Pagina de entregas')