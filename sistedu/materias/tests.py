from django.test import TestCase
from materias.models import Materia
from carreras.models import Carrera, PlanEstudio
from profesor.models import Profesor

class MateriaModelTest(TestCase):
    def setUp(self):
        # Crear Profesor
        self.profesor = Profesor.objects.create(
            nombre="Juan",
            apellido="Perez",
            dni="12345678",
            titulo="Licenciado"
        )
        
        # Crear Carrera
        self.carrera = Carrera.objects.create(
            nombre="Desarrollo de Software",
            codigo="DS01",
            director=self.profesor
        )
        
        # Crear Planes de Estudio
        self.plan2020 = PlanEstudio.objects.create(
            carrera=self.carrera,
            nombre="Plan 2020",
            año_resolucion=2020,
            is_active=False
        )
        
        self.plan2024 = PlanEstudio.objects.create(
            carrera=self.carrera,
            nombre="Plan 2024",
            año_resolucion=2024,
            is_active=True
        )

    def test_materia_creation_and_linking(self):
        # Crear Materia
        materia = Materia.objects.create(
            nombre="Programación III",
            duracion="1 cuatrimestre",
            profesor=self.profesor,
            lugar="Laboratorio A",
            contenido="Desarrollo de aplicaciones avanzadas."
        )
        
        # Asociar a los dos planes de estudio
        materia.planes_estudio.add(self.plan2020, self.plan2024)
        
        # Verificar la relación desde Materia
        self.assertEqual(materia.planes_estudio.count(), 2)
        self.assertIn(self.plan2020, materia.planes_estudio.all())
        self.assertIn(self.plan2024, materia.planes_estudio.all())
        
        # Verificar la relación inversa desde PlanEstudio
        self.assertEqual(self.plan2020.materias.count(), 1)
        self.assertEqual(self.plan2020.materias.first(), materia)

