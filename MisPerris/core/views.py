from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')    

def formulario(request):
    return render(request, 'core/formulario.html')

def regmascota(request):
    return render(request, 'core/regmascota.html')