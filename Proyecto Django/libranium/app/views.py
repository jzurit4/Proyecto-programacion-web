from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/index.html')


def comprar(request):
    return render(request, 'app/comprar.html')

def Crec_Personal(request):
    return render(request, 'app/Crec_Personal.html')


def cuenta(request):
    return render(request, 'app/cuenta.html')

def formulario(request):
    return render(request, 'app/formulario.html')

def juvenil(request):
    return render(request, 'app/juvenil.html')

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
