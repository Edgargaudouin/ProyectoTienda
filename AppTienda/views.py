from http.client import HttpResponse
from django.shortcuts import render
import datetime
from .models import *
from django.template import loader, context, Template
# Create your views here.


"""
def probandohtml(request):

    diccionario = 
    plantilla=loader.get_template('template1.html') #Acá va el archivo HTML que voy a llamar
    documento = plantilla.render(diccionario) #Acá va el contexo a renderizar(es un diccionario context)
    return HTTPResponse(documento)

""" 


