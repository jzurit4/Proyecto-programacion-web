from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    año_pub = models.CharField(max_length=4)
    editorial = models.CharField(max_length=50)
    encuadernacion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="libros",null=True)

    def __str__(self):
        return self.titulo
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    titulo = models.ForeignKey(Libro, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre












