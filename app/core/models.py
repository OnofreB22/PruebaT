from django.core.exceptions import ValidationError
from django.contrib.gis.db import models


class Estacion(models.Model):
    """Estacion Object"""
    nombre = models.CharField(max_length=255)
    ubicacion = models.PointField()

    def __str__(self):
        return self.nombre

    def clean(self):
        super().clean()
        # Validación de coordenadas
        if not (-180 <= self.ubicacion.x <= 180):
            raise ValidationError("La longitud debe estar entre -180 y 180.")
        if not (-90 <= self.ubicacion.y <= 90):
            raise ValidationError("La latitud debe estar entre -90 y 90.")
