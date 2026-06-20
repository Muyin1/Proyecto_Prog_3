from django.contrib import admin
from materias.models import Materia

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'duracion', 'profesor', 'lugar')
    search_fields = ('nombre', 'profesor', 'lugar')
    list_filter = ('duracion',)
