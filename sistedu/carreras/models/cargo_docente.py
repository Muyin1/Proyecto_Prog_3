from django.db import models
from .carrera import Carrera

class CargoDocente(models.Model):
    """
    Representa un cargo institucional, de gestión, investigación o extensión asignado a un profesor dentro de una Carrera.
    Responsabilidad única: Administrar el historial de cargos y resoluciones de los docentes en la carrera (ej. Director de Tesis, Director de Proyectos, Coordinador).
    """
    # Se referencia por string 'authentication.Profesor' para evitar dependencias directas de carga.
    profesor = models.ForeignKey(
        'authentication.Profesor', 
        on_delete=models.CASCADE, 
        related_name='cargos_docentes',
        verbose_name="Docente"
    )
    carrera = models.ForeignKey(
        Carrera, 
        on_delete=models.CASCADE, 
        related_name='cargos_docentes', 
        verbose_name="Carrera"
    )
    nombre_cargo = models.CharField(
        max_length=100, 
        verbose_name="Nombre del Cargo (ej. Director de Tesis)"
    )
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(null=True, blank=True, verbose_name="Fecha de Fin")
    resolucion = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        verbose_name="Resolución de Designación"
    )

    class Meta:
        verbose_name = "Cargo Docente"
        verbose_name_plural = "Cargos Docentes"
        ordering = ['-fecha_inicio']

    def __str__(self):
        vigencia = f"desde {self.fecha_inicio}"
        if self.fecha_fin:
            vigencia += f" hasta {self.fecha_fin}"
        return f"{self.profesor} - {self.nombre_cargo} en {self.carrera.nombre} ({vigencia})"
