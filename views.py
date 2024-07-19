from django.shortcuts import render, redirect, get_object_or_404

from app.carrito import Carrito
from.models import Libro
from .forms import LibroForm

# Create your views here.

def home(request):
    libros = Libro.objects.all() 
    data = {
        'libros':libros
    }

    return render(request, 'app/home.html',data)

def masinfo(request):
    productos = Libro.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/masinfo.html',data)

def nosotros(request):
    return render(request, 'app/nosotros.html')

def carro(request):
    return render(request, 'app/producto/carrito.html')

def agregar_producto(request):

    data = {
        'form': LibroForm()
    }

    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'app/producto/agregar.html', data)


def listar_productos(request):
    productos = Libro.objects.all()

    data = {
        'productos': productos
    }

    return render(request, 'app/producto/listar.html',data)

def modificar_producto(request, id):

    producto = get_object_or_404(Libro, id=id)

    data = {
        'form': LibroForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario
    return render(request,'app/producto/modificar.html', data)


def eliminar_producto(request, id):
    producto = get_object_or_404(Libro, id=id)
    producto.delete()
    return redirect(to="listar_productos")


def agregar_libro(request, libro_id):
    carrito = Carrito(request)
    libro = Libro.objects.get(id=libro_id)
    carrito.agregar(libro)
    return redirect("home")

def eliminar_libro(request, libro_id):
    carrito = Carrito(request)
    libro = Libro.objects.get(id=libro_id)
    carrito.eliminar(libro)
    return redirect("carrito")

def restar_libro(request, libro_id):
    carrito = Carrito(request)
    libro = Libro.objects.get(id=libro_id)
    carrito.restar(libro)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")