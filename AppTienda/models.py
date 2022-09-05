from django.db import models

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()
    costo = models.FloatField()
    precio = models.FloatField()
    rubro = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.codigo) + " " + self.nombre

class Cliente(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    documento = models.IntegerField()
    email = models.EmailField()
    direccion = models.TextField(max_length=200)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + " " + self.apellido + " " + str(self.documento)

class Vendedor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    documento = models.IntegerField()
    codigo = models.IntegerField()
    email = models.EmailField()
    direccion = models.TextField(max_length=200)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.codigo) + " " + self.nombre + " " + self.apellido

class Entrega(models.Model):
    
    fecha_orden = models.DateTimeField()
    fecha_entrega = models.DateField()
    entregado = models.BooleanField(default=False)

    