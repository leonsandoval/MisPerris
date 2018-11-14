from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    path('regmascota/', regmascota, name="regmascota"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('perro_pdf/', perro_pdf, name = "perro_pdf"),
]
