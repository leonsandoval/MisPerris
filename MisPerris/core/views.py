from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')    

def formulario(request): 
    region = Region.objects.all()
    comuna = Comuna.objects.all()
    variables={
        'region':region,
        'comuna':comuna
    }
    return render(request, 'core/formulario.html', variables)

def regmascota(request):
    raza = Raza.objects.all()
    estado = Estado.objects.all()
    variables={
        'raza':raza,
        'estado':estado
    }
    if request.POST:
        mascota = Mascota()
        mascota.nombre=request.POST.get('txtNombre')
        raza = Raza()
        raza.id = int(request.POST.get('cboRaza'))
        mascota.genero = request.POST.get('rbGenero')

        try:
            mascota.save()
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"
    return render(request, 'core/regmascota.html',variables)


