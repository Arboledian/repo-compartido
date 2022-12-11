from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from gestionpedidos.forms import RegForm 
from gestionpedidos.models import registrado
from gestionpedidos.models import Articulos

# Create your views here.
def busqueda_productos(request):
    return render(request, "busqueda_productos.html" )

def buscar(request):
    if request.GET["prd"]:
    
       producto=request.GET["prd"]
       if len(producto)>20:
            mensaje="Texto demasiado largo"

       else:

            articulos=Articulos.objects.filter(nombre__icontains=producto)#funciona como like de sql
            return render(request, "resultado_busqueda.html", {"articulos": articulos, "query":producto})

    else:
        
        mensaje="NO se han ingresado criterios de busqueda"

    return HttpResponse(mensaje)
    

def inicio(request):
    form=RegForm(request.POST or None)
    if form.is_valid():
        form_data= form.cleaned_data
        abc= form_data.get("email")
        nombre=form_data.get("nombre")
        #edad=form_data.get("edad")
        obj=registrado.objects.create(email=abc, nombre=nombre)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    context={"elform": form}
    return render(request, "inicio.html",context)

def buscar2(request):

    if request.GET["nome"]:

       user=request.GET["nome"]

       if len(user)>20:
            mensaje="Texto demasiado largo"
       else:

            usernames=registrado.objects.filter(nombre__icontains=user)
            return render(request, "busqueda_user.html", {"registrado": usernames, "query":user})
    else:
        
        usernames = registrado.objects.all().order_by("-id")
        return render(request, "busqueda_user.html",{"registrado":usernames})
        

def delete(request, id):
    user = registrado.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def update(request, id):
        if request.GET["name"]:
            user=request.GET["name"]        
            _nombre=user
            newuser= registrado.objects.get(id=id)
            newuser.nombre = _nombre
            newuser.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))





    


    	
    #return HttpResponse(mensaje)
    
#update ser como:
#variablelocal.valor= "nuevovalor"
#variablelocal.save()
#delete ser como:
#variablelocal.object.get(id=x)
#variablelocal.delete()

#in template
# {% for order in user.order_set.all %}
#    <p>{{ order.order_number }}</p>
#{% endfor %}
