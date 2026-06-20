from django.db import models
from profesor.models import Profesor

class Materia(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    duracion = models.CharField(max_length=100, verbose_name="Duración", help_text="Ej. 64 horas, 1 cuatrimestre")
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Profesor", related_name="materias")
    lugar = models.CharField(max_length=200, verbose_name="Lugar", blank=True, null=True, help_text="Ej. Aula 102, Laboratorio B")
    contenido = models.TextField(verbose_name="Contenido", blank=True, null=True)

    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materias"

    def __str__(self):
        return self.nombre
