from django.urls import path
from AppTienda.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('producto/', producto, name= 'producto'),
    path('cliente/', cliente, name= 'cliente'),
    path('vendedor/', vendedor, name= 'vendedor'),
    path('entrega/', entrega, name= 'entrega'),
    path('clienteFormulario/', clienteForm, name='clienteFormulario' ),
    path('productoFormulario/', productoForm, name='productoFormulario'),
    path('vendedorFormulario/', vendedorForm, name='vendedorFormulario' ),
    path('listar-clientes/', listarClientes, name='listarClientes'),
    path('buscarClientes/', buscarClientes, name='buscarClientes'),
    path('buscar/', buscar),
]



 