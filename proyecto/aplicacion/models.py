from django.db import models

# Create your models here.
class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()

    class Meta:
        ordering = ['nombre']

    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Turno(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()
    fecha = models.DateField()

