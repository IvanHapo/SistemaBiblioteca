from django.db import models
from django.core.validators import MaxValueValidator


class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=50)
    edad = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    anio_fundacion = models.IntegerField()
    direccion = models.TextField()
    sitio_web = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    anio_publicacion = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
