from django.shortcuts import render
from django.http import HttpResponse
from gestionpedidos.models import Articulos
# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html" )

def buscar(request):
    if request.GET["prd"]:

       #mensaje="Articulo buscado: %r" %request.GET["prd"] esta linea es para llamar al dato ingresado, pero NO esta conectado con la BD 
       producto=request.GET["prd"]
       if len(producto)>20:
            mensaje="Texto demasiado largo"

       else:

            articulos=Articulos.objects.filter(nombre__icontains=producto)#funciona como like de sql
            return render(request, "resultado_busqueda.html", {"articulos": articulos, "query":producto})

    else:
        
        mensaje="NO se han ingresado criterios de busqueda"

    return HttpResponse(mensaje)