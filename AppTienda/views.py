
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import *
from django.template import loader, context, Template
# Create your views here.


def inicio(request):
    return render (request, 'AppTienda/inicio.html') #Tengo que crear un template inicio

def producto(request):
    return render (request, 'AppTienda/producto.html')

def cliente(request):
    return render (request, 'AppTienda/cliente.html')

def vendedor(request):
    return render (request, 'AppTienda/vendedor.html')

def entrega(request):
    return render (request, 'AppTienda/entrega.html')