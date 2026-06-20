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
            "El DNI solo debe contener números."
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

