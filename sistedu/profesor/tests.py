from django.test import TestCase
from django.core.exceptions import ValidationError
from profesor.models import Profesor

class ProfesorModelTest(TestCase):
    def test_dni_only_numbers_is_valid(self):
        profesor = Profesor(
            nombre="Juan",
            apellido="Perez",
            dni="12345678",
            titulo="Licenciado"
        )
        # Should not raise any validation error
        profesor.full_clean()

    def test_dni_with_letters_is_invalid(self):
        profesor = Profesor(
            nombre="Juan",
            apellido="Perez",
            dni="12345678A",
            titulo="Licenciado"
        )
        with self.assertRaises(ValidationError) as context:
            profesor.full_clean()
        
        self.assertIn('dni', context.exception.message_dict)
        self.assertEqual(
            context.exception.message_dict['dni'][0],
            "El DNI solo puede contener números."
        )

    def test_dni_with_spaces_is_invalid(self):
        profesor = Profesor(
            nombre="Juan",
            apellido="Perez",
            dni="1234 5678",
            titulo="Licenciado"
        )
        with self.assertRaises(ValidationError) as context:
            profesor.full_clean()
        
        self.assertIn('dni', context.exception.message_dict)


class ProfesorViewsTest(TestCase):
    def setUp(self):
        self.profesor = Profesor.objects.create(
            nombre="Juan",
            apellido="Perez",
            dni="12345678",
            titulo="Licenciado"
        )

    def test_list_view(self):
        response = self.client.get('/profesores/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Juan")
        self.assertContains(response, "Perez")

    def test_create_view_get(self):
        response = self.client.get('/profesores/nuevo/')
        self.assertEqual(response.status_code, 200)

    def test_create_view_post(self):
        data = {
            'nombre': 'Maria',
            'apellido': 'Gomez',
            'dni': '87654321',
            'titulo': 'Ingeniera'
        }
        response = self.client.post('/profesores/nuevo/', data)
        self.assertRedirects(response, '/profesores/')
        self.assertTrue(Profesor.objects.filter(dni='87654321').exists())

    def test_update_view_get(self):
        response = self.client.get(f'/profesores/editar/{self.profesor.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_update_view_post(self):
        data = {
            'nombre': 'Juan Carlos',
            'apellido': 'Perez',
            'dni': '12345678',
            'titulo': 'Licenciado'
        }
        response = self.client.post(f'/profesores/editar/{self.profesor.pk}/', data)
        self.assertRedirects(response, '/profesores/')
        self.profesor.refresh_from_db()
        self.assertEqual(self.profesor.nombre, 'Juan Carlos')

    def test_delete_view_get(self):
        response = self.client.get(f'/profesores/eliminar/{self.profesor.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_delete_view_post(self):
        response = self.client.post(f'/profesores/eliminar/{self.profesor.pk}/')
        self.assertRedirects(response, '/profesores/')
        self.assertFalse(Profesor.objects.filter(pk=self.profesor.pk).exists())


