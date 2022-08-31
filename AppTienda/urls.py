from django.urls import path
from AppTienda.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('producto/', producto, name= 'producto'),
    path('cliente/', cliente, name= 'cliente'),
    path('vendedor/', vendedor, name= 'vendedor'),
    path('entrega/', entrega, name= 'entrega'),
]



