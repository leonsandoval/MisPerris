from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

def home(request):
    perros = Mascota.objects.filter(estado=3)
    return render(request, 'core/home.html', 
    {
    'adoptados':perros
    })

def galeria(request):
    perros = Mascota.objects.filter(estado=1)
    return render(request, 'core/galeria.html', 
    {
    'rescatados':perros
    })    

def formulario(request): 
    region = Region.objects.all()
    comuna = Comuna.objects.all()
    variables={
        'region':region,
        'comuna':comuna
    }
    return render(request, 'core/formulario.html', variables)

# @login_required


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
        raza.id = request.POST.get('cboRaza')
        mascota.raza = raza
        genero = request.POST.get('rbGenero')
        mascota.genero = genero
        mascota.fechaIngreso= request.POST.get('txtFecIngreso')
        mascota.fechaNacimiento = request.POST.get('txtFecNacimiento')
        mascota.descripcion = request.POST.get('txtDescripcion')
        mascota.foto =  request.FILES.get('imgFoto')
        estado = Estado()
        estado.id = int(request.POST.get('cboEstado'))
        mascota.estado= estado  
        mascota.save() 

        try:
                       
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"
    return render(request, 'core/regmascota.html',variables)



def eliminar(request, id):

    #para eliminar es necesario primero buscar el automovil
    perro = Mascota.objects.get(id=id)

    #una vez encontrado el automovil se procede a eliminarlo
    try:
        perro.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje ="No se ha podido eliminar"
        messages.error(request, mensaje)
        
    #el redirect lo redirige por alias de una ruta
    return redirect(to="galeria")

def modificar(request, id):

    raza = Raza.objects.all()
    estado = Estado.objects.all()
   
    mascota = Mascota.objects.get(id=id)
    variables = {
        'raza':raza,
        'estado':estado,
        'm': mascota
    }

    if request.POST:
        #si la peticion es POST recibimos las variables
        mascota.id = id
        mascota = Mascota()
        mascota.nombre=request.POST.get('txtNombre')
        raza = Raza()
        raza.id = request.POST.get('cboRaza')
        mascota.raza = raza
        genero = request.POST.get('rbGenero')
        mascota.genero = genero
        mascota.fechaIngreso= request.POST.get('txtFecIngreso')
        mascota.fechaNacimiento = request.POST.get('txtFecNacimiento')
        mascota.descripcion = request.POST.get('txtDescripcion')
        mascota.foto = request.POST.get('imgFoto')
        estado = Estado()
        estado.id = int(request.POST.get('cboEstado'))
        mascota.estado= estado  

        #ahora procederemos a actualizar el automovil
        try:
            mascota.save()
            messages.success(request, "Actualizado correctamente")
        except:
            messages.error(request, "No se ha podido actualizar")

        #le haremos un redirect al usuario de vuelta hacia el listado   
    return render(request, 'core/modificar.html', variables)




