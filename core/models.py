from django.db import models

# Create your models here.
class Ciudad(models.Model):
    foto = models.ImageField(upload_to='ciudades/')
    nombre = models.CharField (max_length=25)
    fecha_fundacion = models.DateField()
    poblacion = models.PositiveBigIntegerField()
    lugares = models.TextField()

    def __str__(self):
        return self.nombre

