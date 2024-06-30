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
    


opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "sugerencia"],
    [3, "otros"],
]


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje= models.TextField()
    tipo = models.IntegerField(choices=opciones_consultas)
    

    def __str__(self):
        return self.nombre