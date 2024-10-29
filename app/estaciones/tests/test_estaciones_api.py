from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Estacion


class EstacionesApiTests(TestCase):
    """ Tests para los endpoints de la API"""

    def setUp(self):
        self.client = APIClient()

    def test_create_estacion(self):
        """Test de creacion de una nueva estacion."""
        url = reverse('estacion-list')
        data = {
            'nombre': 'New York',
            'ubicacion': 'POINT(-73.935242 40.73061)'
        }

        response = self.client.post(url, data, format='json')

        # Verificar que se haya creado la estacion
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Estacion.objects.count(), 1)
        self.assertEqual(Estacion.objects.get().nombre, 'New York')
        self.assertEqual(Estacion.objects.get().ubicacion.x, -73.935242)
        self.assertEqual(Estacion.objects.get().ubicacion.y, 40.73061)

    def test_create_invalid_estacion(self):
        """Test de creación de una estación con valores de longitud y latitud fuera de rango."""
        url = reverse('estacion-list')
        data = {
            'nombre': 'Estacion Invalida',
            'ubicacion': 'POINT(-300 300)'  # Valores fuera de rango
        }

        response = self.client.post(url, data, format='json')

        # Verificar que la creación no sea exitosa y arroje un error de validación
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Estacion.objects.count(), 0)

    def test_list_estaciones(self):
        """Test para listar todas las estaciones."""
        Estacion.objects.create(nombre='New York', ubicacion='POINT(-73.935242 40.73061)')
        Estacion.objects.create(nombre='Medellin', ubicacion='POINT(-75.56959104387936 6.1922579572101855)')

        url = reverse('estacion-list')
        response = self.client.get(url)

        # Verificar que se devuelvan las estaciones
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_estacion_cercana(self):
        """Test para obtener la estacion más cercana."""
        estacion1 = Estacion.objects.create(nombre='Medellin', ubicacion='POINT(-75.56959104387936 6.1922579572101855)')
        estacion2 = Estacion.objects.create(nombre='Envigado', ubicacion='POINT(-75.58752264870299 6.170063820656889)')
        estacion3 = Estacion.objects.create(nombre='Bogota', ubicacion='POINT(-74.03616403078435 4.726529812472924)')

        # La ubicación de la estacion a la que estamos buscando la mas cercana
        url = reverse('estacion-cercana', args=[estacion1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], estacion2.id)
