
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import *
from django.template import loader, context, Template
# Create your views here.


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