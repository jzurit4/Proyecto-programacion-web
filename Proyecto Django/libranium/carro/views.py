from django.shortcuts import render
from .carro import Carro

from app.models import Libro

from django.shortcuts import redirect
# Create your views here.

def agregar_producto(request, producto_id):

    carro=Carro(request)

    producto=Libro.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("home")

def eliminar_producto(request, producto_id):

    carro=Carro(request)

    producto=Libro.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("home")

def restar_producto(request, producto_id):

    carro=Carro(request)

    producto=Libro.objects.get(id=producto_id)

    carro.restar(producto=producto)

    return redirect("home") 

def limpiar_carro(request, producto_id):

    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("home")