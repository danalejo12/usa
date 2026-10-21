from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Ciudad


# Mostrar todas las ciudades
def inicio(request):
    ciudades = Ciudad.objects.all()

    return render(request, 'core/inicio.html', {
        'ciudades': ciudades
    })


# Mostrar una ciudad específica
def detalle_ciudad(request, id):
    ciudad = get_object_or_404(Ciudad, id=id)

    return render(request, 'core/detalle_ciudad.html', {
        'ciudad': ciudad
    })
