from django.contrib import admin
from carreras.models import Carrera, PlanEstudio, CargoDocente

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'director')
    search_fields = ('nombre', 'codigo', 'director__nombre', 'director__apellido')

@admin.register(PlanEstudio)
class PlanEstudioAdmin(admin.ModelAdmin):
    list_display = ('carrera', 'nombre', 'año_resolucion', 'is_active')
    list_filter = ('carrera', 'is_active')
    search_fields = ('nombre', 'carrera__nombre')

@admin.register(CargoDocente)
class CargoDocenteAdmin(admin.ModelAdmin):
    list_display = ('profesor', 'carrera', 'nombre_cargo', 'fecha_inicio', 'fecha_fin')
    list_filter = ('carrera', 'nombre_cargo')
    search_fields = ('profesor__nombre', 'profesor__apellido', 'nombre_cargo')
