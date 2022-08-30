from django.urls import path
from AppTienda.views import *

urlpatterns = [
    path('', inicio),
    path('producto/', producto),
    path('cliente/', cliente),
    path('vendedor/', vendedor),
    path('entrega/', entrega),
]



