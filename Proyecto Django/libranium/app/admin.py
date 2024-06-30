from django.contrib import admin
from .models import Genero, Producto,Contacto
# Register your models here.

admin.site.register(Genero)
admin.site.register(Producto)
admin.site.register(Contacto)