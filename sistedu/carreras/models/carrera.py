from django.db import models

class Carrera(models.Model):

    nombre = models.CharField(max_length=150, verbose_name="Nombre de la Carrera")
    codigo = models.CharField(max_length=20, unique=True, verbose_name="Código de Carrera")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    
    # Se referencia por string 'profesor.Profesor' para evitar acoplamiento fuerte e importaciones circulares.
    # El director es un profesor asignado al cargo de conducción académica de la carrera.
    director = models.ForeignKey(
        'profesor.Profesor', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='carreras_dirigidas',
        verbose_name="Director de Carrera"
    )

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
