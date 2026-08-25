from django.contrib import admin
from materias.models import Materia

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion', 'profesor', 'lugar')
    search_fields = ('nombre', 'profesor__nombre', 'profesor__apellido', 'lugar')
    list_filter = ('duracion', 'planes_estudio')
    filter_horizontal = ('planes_estudio',)
