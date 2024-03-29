from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    tfno=models.CharField(max_length=30)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
    
    
class registrado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    email=models.EmailField()

    def __unicode__(self):
        return self.email
    
    def __str__(self):
        return self.email
