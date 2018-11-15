from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest
import json
from core.models import Mascota
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def listar_mascotas(request):
    mascotas = Mascota.objects.all()

    #transformamos el arreglo de Mascota
    #a un json
    mascotasJson = serializers.serialize('json', mascotas)

    #retornamos el json como respuesta al usuario
    return HttpResponse(mascotasJson, content_type="application/json")


@csrf_exempt
@require_http_methods(['POST'])
def agregar_mascota(request):
    #obtener el body del request donde esta el json
    body  = request.body.decode('utf-8')

    #ahora transformamos el body hacia un diccionario de python
    body_diccionario = json.loads(body)

    #ingresamos los datos a la BBDD
    mascota = Mascota()
    mascota.nombre = body_diccionario['nombre']
    mascota.raza = body_diccionario['raza']
    mascota.genero = body_diccionario['genero']
    mascota.fechaIngreso = body_diccionario['fechaIngreso']
    mascota.fechaNacimiento = body_diccionario['fechaNacimiento']
    mascota.descripcion = body_diccionario['descripcion']
    mascota.foto = body_diccionario['foto']
    mascota.estado = body_diccionario['estado']


    try:
        mascota.save()
        mensaje = {
            'mensaje':'guardado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type="application/json")
    except:
        mensaje = {
            'mensaje':'error al guardar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type="application/json")


@csrf_exempt
@require_http_methods(['PUT'])
def modificar_mascota(request):
    #obtener el body del request donde esta el json
    body  = request.body.decode('utf-8')

    #ahora transformamos el body hacia un diccionario de python
    body_diccionario = json.loads(body)

    #ingresamos los datos a la BBDD
    mascota = Mascota()
    mascota.id = body_diccionario['id']
    #mascota.patente = body_diccionario['patente']
    mascota.modelo = body_diccionario['modelo']
    mascota.anio = body_diccionario['anio']
    mascota.marca = Marca(id=body_diccionario['marca_id'])

    try:
        mascota.save()
        mensaje = {
            'mensaje':'modificado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type="application/json")
    except:
        mensaje = {
            'mensaje':'error al modificar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type="application/json")

@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_mascota(request, id):

    try:
        mascota = Mascota.objects.get(id=id)
        mascota.delete()
        mensaje = {
            'mensaje':'Eliminado correctamente'
        }
        return HttpResponse(json.dumps(mensaje), content_type='application/json')
    except:
        mensaje = {
            'mensaje': 'No se ha podido eliminar'
        }
        return HttpResponseBadRequest(json.dumps(mensaje), content_type='application/json')