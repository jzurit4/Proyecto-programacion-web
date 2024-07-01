from django.contrib import admin
from .models import Libro,Categoria
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["titulo","autor","precio","descripcion","editorial","encuadernacion"]
    list_editable = ["precio"]
    search_fields = ["titulo","autor"]
    list_filter = ["autor","editorial","encuadernacion"]
    list_per_page = 5



admin.site.register(Libro, ProductoAdmin)
admin.site.register(Categoria)











