from django.db import models

# Create your models here.


class Genero(models.Model):
    tipo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipo
    

    
class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    precio = models.IntegerField()
    autor = models.CharField(max_length=50)
    sinopsis = models.TextField()
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)
    
    def __str__(self):
        return self.titulo
    

opciones_c = [
    [0, "Consultas"],
    [1, "Reclamos"],
    [2, "Sugerencias"],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipoCon= models.IntegerField(choices=opciones_c)
    mensaje =models.TextField()

    def __str__(self):
        return self.nombre