from django import forms

class clienteFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    documento = forms.IntegerField()
    email = forms.EmailField()
    direccion = forms.CharField(max_length=200)
    

