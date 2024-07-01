from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from .forms import ContactoForm, CustomUserCreationForm, LibroForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

def home(request):
    productos = Libro.objects.all() 
    data = {
        'productos':productos
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
    productos = Libro.objects.all()
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

@permission_required('app.add_libro')
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
    
    return render(request, 'app/produc/agregar.html', data)

@permission_required('app.view_libro')
def listar_productos(request):
    productos = Libro.objects.all()

    data = {
        'productos': productos
    }

    return render(request, 'app/produc/listar.html',data)

@permission_required('app.change_libro')
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
    return render(request,'app/produc/modificar.html', data)

@permission_required('app.delete_libro')
def eliminar_producto(request, id):
    producto = get_object_or_404(Libro, id=id)
    producto.delete()
    return redirect(to="listar_productos")