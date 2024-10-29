"""Test para los modelos"""
from django.test import TestCase

from core import models

from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError


class ModelTests(TestCase):

    def test_create_estacion(self):
        """Test para crear una estacion con exito."""
        estacion = models.Estacion.objects.create(
            nombre="Estacion 4",
            ubicacion=Point(-74.0060, 40.7128),
        )

        self.assertEqual(str(estacion), estacion.nombre)
        self.assertEqual(estacion.nombre, "Estacion 4")
        self.assertIsInstance(estacion.ubicacion, Point)

    def test_estacion_str_method(self):
        """Test para verificar que el string devuelve el nombre correcto."""
        estacion = models.Estacion.objects.create(
            nombre="Estacion de Prueba",
            ubicacion=Point(-74.0060, 40.7128),
        )
        self.assertEqual(str(estacion), "Estacion de Prueba")

    def test_estacion_lat_long_validation(self):
        """Test para verificar que las coordenadas estan en el rango correcto."""
        estacion_invalida = models.Estacion(
        nombre="Estacion Invalida",
        ubicacion=Point(-200, 100)  # Fuera del rango válido
        )

        with self.assertRaises(ValidationError):
            estacion_invalida.full_clean()
