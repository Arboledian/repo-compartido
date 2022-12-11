from django.contrib import admin
from .models import registrado
# Register your models here.
class Adminregistrado(admin.ModelAdmin):
    list_display=["__unicode__", "nombre"]
    class Meta:
        model=registrado
admin.site.register(registrado, Adminregistrado)
