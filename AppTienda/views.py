
import email
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import *
from django.template import loader, context, Template
#Formularios
from AppTienda.forms import clienteFormulario, productoFormulario, vendedorFormulario

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
            data = miFormulario.cleaned_data # -> Me genera un diccionario puedo nombre = data["nombre"]
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

def productoForm(request):

    if request.method =="POST":
        miFormulario = productoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data # -> Me genera un diccionario puedo nombre = data["nombre"]
            print(data)
            nombre = data["nombre"]
            codigo = data["codigo"]
            costo = data["costo"]
            precio = data["precio"]
            rubro = data["rubro"]
            descripcion = data ["descripcion"]
            estado = data["estado"]
            producto = Producto(nombre=nombre, codigo = codigo, costo = costo, precio = precio, rubro = rubro, descripcion = descripcion, estado = estado)
            producto.save()
            return render(request, 'AppTienda/inicio.html', {"mensaje": "Producto creado"}) #Este mensaje debe crearse en el template con jinja {}
        else:
            return render(request, 'AppTienda/inicio.html', {"mensaje": "Error"})
    
    else:
        miFormulario=productoFormulario()
        return render(request, 'AppTienda/productoFormulario.html', {"formulario" : miFormulario})

def vendedorForm(request):

    if request.method =="POST":
        miFormulario = vendedorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data # -> Me genera un diccionario puedo nombre = data["nombre"]
            print(data)
            nombre = data["nombre"]
            apellido = data["apellido"]
            documento = data["documento"]
            codigo = data["codigo"]
            email = data["email"]
            direccion = data ["direccion"]
            estado = data["estado"]
            vendedor= Vendedor(nombre=nombre, apellido = apellido, documento = documento, codigo = codigo, email = email, direccion = direccion, estado = estado)
            vendedor.save()
            return render(request, 'AppTienda/inicio.html', {"mensaje": "Vendedor creado"}) #Este mensaje debe crearse en el template con jinja {}
        else:
            return render(request, 'AppTienda/inicio.html', {"mensaje": "Error"})
    
    else:
        miFormulario=vendedorFormulario()
        return render(request, 'AppTienda/vendedorFormulario.html', {"formulario" : miFormulario})