from email.policy import default
from xml.dom.minidom import Document
from django import forms

class clienteFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    documento = forms.IntegerField()
    email = forms.EmailField()
    direccion = forms.CharField(max_length=200)
    
class productoFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    codigo = forms.IntegerField()
    costo = forms.FloatField()
    precio = forms.FloatField()
    rubro = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=200)
    estado = forms.BooleanField()
    
class vendedorFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    documento = forms.IntegerField()
    codigo = forms.IntegerField()
    email = forms.EmailField()
    direccion = forms.CharField(max_length=200)
    estado = forms.BooleanField()
    