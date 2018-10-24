from django.db import models
from django import forms

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=25)
    clave = models.CharField(max_length=25)
    pregunta_secreta = models.CharField(max_length=100)
    respuesta_secreta = models.CharField(max_length=50)
    
    def __str__(self):
        return self.usuario

class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    # nRegion = models.IntegerField()
    def __str__(self):
        return self.nombre

class Region(models.Model):
    nombre = models.CharField(max_length=50)
    # comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regiones"

class Persona(models.Model):
    rut = models.IntegerField()
    rut_dv = models.CharField(max_length=1)
    email = models.EmailField( max_length=254)
    nombreCompleto = models.CharField(max_length=150)
    fechaNacimiento = models.DateField(auto_now=False, auto_now_add=False)
    telefono = models.IntegerField()
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    tipoVivienda = models.CharField( max_length=50)
    # nombre = models.CharField(max_length=50)
    # apellido = models.CharField(max_length=50)
    # direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Suscripcion(models.Model):
    n_suscripcion = models.AutoField(primary_key=True)
    abono = models.IntegerField()
    fechaPago = models.DateField()

    def __str__(self):
        return self.n_suscripcion

    class Meta:
        verbose_name = "Suscripcion"
        verbose_name_plural = "Suscripciones"

class Campania(models.Model):
    identificador = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()
    slogan = models.CharField(max_length=150)

    def __str__(self):
        return self.identificador


class Publicidad(models.Model):
    identificador = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='publi')
    logo = models.CharField(max_length=50)

    def __str__(self):
        return self.identificador

    class Meta:
        verbose_name = "Publicidad"
        verbose_name_plural = "Publicidad"

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

class Raza(models.Model):
    nombre = models.CharField( max_length=50)
    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField( max_length=50)
    def __str__(self):
        return self.nombre


GENERO_RADIO = (
        (1,'Macho'),
        (2,'Hembra'),
    )

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    genero = forms.ChoiceField(choices = GENERO_RADIO, widget=forms.RadioSelect())
    fechaIngreso = models.DateField()
    fechaNacimiento = models.DateField(null=True)
    descripcion = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='pets')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    # rut_m = models.CharField(max_length=15)
    # edad = models.IntegerField()
    # raza = models.CharField(max_length=25)
    # chip = models.BooleanField()
    # n_chip = models.IntegerField()
    # tipo = models.CharField(max_length=50)


class AtencionMascota(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    diagnostico = models.CharField(max_length=150)

