from django.db import models

class registrado(models.Model):
    nombre=models.CharField(max_length=100)
    email=models.EmailField()

    def __unicode__(self):
        return self.email
    
    def __str__(self):
        return self.email
# Create your models here.
