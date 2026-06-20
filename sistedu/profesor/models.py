from django.core.validators import RegexValidator
from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    
    dni_validator = RegexValidator(
        regex=r'^[0-9]+$',
        message="El DNI solo puede contener números."
    )
    dni = models.CharField(
        max_length=20, 
        unique=True, 
        verbose_name="DNI",
        validators=[dni_validator]
    )
    titulo = models.CharField(max_length=200, verbose_name="Título")

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
