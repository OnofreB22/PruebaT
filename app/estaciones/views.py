from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError as DRFValidationError

from django.contrib.gis.db.models.functions import Distance

from core.models import Estacion
from .serializers import EstacionSerializer


class EstacionListCreateAPIView(generics.ListCreateAPIView):
    """Vista para listar y crear estaciones"""
    queryset = Estacion.objects.all()
    serializer_class = EstacionSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except DRFValidationError as e:
            return Response({'error': e.message_dict}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Ha ocurrido un error al crear la estación.'}, status=status.HTTP_400_BAD_REQUEST)


class EstacionCercanaAPIView(generics.GenericAPIView):
    """Vista para obtener la estacion más cercana a una estacion específica"""

    def get(self, request, id, *args, **kwargs):
        try:
            # Obtener la estacion por ID
            estacion_base = Estacion.objects.get(id=id)

            # Obtener la estacion más cercana
            estacion_cercana = Estacion.objects.exclude(id=id).annotate(
                distance=Distance('ubicacion', estacion_base.ubicacion)
            ).order_by('distance').first()

            if estacion_cercana:
                serializer = EstacionSerializer(estacion_cercana)
                return Response(serializer.data)
            else:
                return Response({"error": "No hay estaciones cercanas."}, status=status.HTTP_404_NOT_FOUND)
        except Estacion.DoesNotExist:
            return Response({"error": "Estacion no encontrada."}, status=status.HTTP_404_NOT_FOUND)
