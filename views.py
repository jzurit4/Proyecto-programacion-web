from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def masinfo(request):
    return render(request, 'app/masinfo.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')