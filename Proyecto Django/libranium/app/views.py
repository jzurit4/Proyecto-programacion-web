from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, CustomUserCreationForm, ProductoForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/index.html',data)

def comprar(request):
    return render(request, 'app/comprar.html')

def Crec_Personal(request):
    return render(request, 'app/Crec_Personal.html')

def Cuenta(request):
    return render(request, 'app/cuenta.html')

def login(request):
    return render(request, 'registration/login.html')

def formulario(request): 
    data = {
        'form' :ContactoForm()
    }    

    if request.method =='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto recibido!"
        else:
            data["form"] = formulario
    return render(request, 'app/formulario.html',data)

def juvenil(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/juvenil.html', data)

def libro1(request):
    return render(request, 'app/libro1.html')

def Lit_Chilena(request):
    return render(request, 'app/Lit_Chilena.html')

def Nosotros(request):
    return render(request, 'app/Nosotros.html')

def novelas(request):
    return render(request, 'app/novelas.html')

def poesia(request):
    return render(request, 'app/poesia.html')

def ubicacion(request):
    return render(request, 'app/ubicacion.html')


def registro(request):
    data = {
        'form':CustomUserCreationForm()
    }
    if request.method =='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request)
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


def agregarProducto(request):
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto agregado correctamente!"
        else:
            data["form"] = formulario
    return render(request, 'app/produc/agregar.html',data)

def listar_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request, 'app/produc/listar.html',data)


def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)
    
    data = {
        'form':ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
    return render(request, 'app/produc/editar.html',data)