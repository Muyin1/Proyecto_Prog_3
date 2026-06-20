from .carrera import Carrera
from .plan_estudio import PlanEstudio
from .cargo_docente import CargoDocente

# Exponemos de forma explícita las clases para que Django ORM las reconozca al importar el paquete
__all__ = ['Carrera', 'PlanEstudio', 'CargoDocente']
