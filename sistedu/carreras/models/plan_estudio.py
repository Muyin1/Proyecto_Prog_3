from django.db import models
from .carrera import Carrera

class PlanEstudio(models.Model):
    """
    Representa una resolución o versión de plan de estudio específica para una Carrera.
    Responsabilidad única: Agrupar y definir la vigencia temporal y estado de la estructura curricular de una carrera.
    """
    carrera = models.ForeignKey(
        Carrera, 
        on_delete=models.CASCADE, 
        related_name='planes_estudio', 
        verbose_name="Carrera"
    )
    nombre = models.CharField(max_length=100, verbose_name="Nombre/Código del Plan (ej. Plan 2024)")
    año_resolucion = models.PositiveIntegerField(verbose_name="Año de la Resolución")
    is_active = models.BooleanField(
        default=True, 
        verbose_name="Está Activo",
        help_text="Define si las nuevas inscripciones a la carrera se realizarán bajo este plan de estudios."
    )

    class Meta:
        verbose_name = "Plan de Estudio"
        verbose_name_plural = "Planes de Estudio"
        ordering = ['-año_resolucion', 'nombre']

    def __str__(self):
        estado = "Activo" if self.is_active else "Inactivo"
        return f"{self.carrera.nombre} - {self.nombre} ({estado})"
