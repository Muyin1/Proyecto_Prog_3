from django.contrib import admin
from profesor.models import Profesor

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'dni', 'titulo')
    search_fields = ('apellido', 'nombre', 'dni', 'titulo')
