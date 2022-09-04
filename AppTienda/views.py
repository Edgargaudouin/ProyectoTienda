
import email
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import *
from django.template import loader, context, Template
#Formularios
from AppTienda.forms import clienteFormulario

def inicio(request):
    return render (request, 'AppTienda/inicio.html') #Tengo que crear un template inicio

def producto(request):                                  #Para usar los valores generados puedo crear una lista listita
    return render (request, 'AppTienda/producto.html') #return render (request, 'AppTienda/producto.html', {"listita": lista}) 

def cliente(request):
    return render (request, 'AppTienda/cliente.html')

def vendedor(request):
    return render (request, 'AppTienda/vendedor.html')

def entrega(request):
    return render (request, 'AppTienda/entrega.html')


#Creando formularios
def clienteForm(request):

    if request.method =="POST":
        miFormulario = clienteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            print(data)
            nombre = data.get("nombre")
            apellido = data.get("apellido")
            documento = data.get("documento")
            email = data.get("email")
            direccion = data.get("direccion")
            cliente = Cliente(nombre=nombre, apellido=apellido, documento=documento, email=email, direccion=direccion)
            cliente.save()
            return render(request, 'AppTienda/inicio.html', {"mensaje": "Cliente creado"}) #Este mensaje debe crearse en el template con jinja {}
        else:
            return render(request, 'AppTienda/inicio.html', {"mensaje": "Error"})
    
    else:
        miFormulario=clienteFormulario()
        return render(request, 'AppTienda/clienteFormulario.html', {"formulario" : miFormulario})
    