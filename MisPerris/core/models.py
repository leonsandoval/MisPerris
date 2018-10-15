from django.db import models

# Create your models here.

class Usuario(models.Model):
    clave = models.CharField(max_length=25)
    pregunta_secreta = models.CharField(max_length=100)
    respuesta_secreta = models.CharField(max_length=50)
    email = models.EmailField()

class Persona(models.Model):
    rut = models.IntegerField()
    rut_dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)

class Suscripcion(models.Model):
    n_suscripcion = models.AutoField(primary_key=True)
    abono = models.IntegerField()
    fechaPago = models.DateField()


class Campania(models.Model):
    identificador = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()
    slogan = models.CharField(max_length=150)

class Publicidad(models.Model):
    identificador = models.AutoField(primary_key=True)
    imagen = models.ImageField()
    logo = models.CharField(max_length=50)

class Refugio(models.Model):
    identificador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()

class GastoMensual(models.Model):
    nombre = models.CharField(max_length=50)
    fechaPago = models.DateField()
    tipo = models.CharField(max_length=50)

class Suministro(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    fecha = models.DateField()
    tipo = models.CharField(max_length=50)

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    rut_m = models.CharField(max_length=15)
    edad = models.IntegerField()
    raza = models.CharField(max_length=25)
    chip = models.BooleanField()
    n_chip = models.IntegerField()
    tipo = models.CharField(max_length=50)

class AtencionMascota(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    diagnostico = models.CharField(max_length=150)

class Comuna(models.Model):
    nombre = models.CharField(max_length=50)

class Region(models.Model):
    nombre = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
