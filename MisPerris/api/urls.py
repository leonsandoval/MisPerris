from django.urls import path
from .views import listar_mascotas, agregar_mascota, modificar_mascota, eliminar_mascota

urlpatterns = [
    path('mascota/', listar_mascotas, name="api_listar_mascotas"),
    path('mascota/agregar/', agregar_mascota, name="api_agregar_mascota"),
    path('mascota/<id>/modificar/', modificar_mascota, name="api_modificar_mascota"),
    path('mascota/<id>/eliminar/', eliminar_mascota, name="api_eliminar_mascota"),
]