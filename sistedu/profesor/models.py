from django.core.validators import RegexValidator
from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    dni = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="DNI",
        validators=[
            RegexValidator(
                regex=r'^\d+$',
                message="El DNI solo debe contener números.",
                code="invalid_dni"
            )
        ]
    )
    titulo = models.CharField(max_length=200, verbose_name="Título")

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
