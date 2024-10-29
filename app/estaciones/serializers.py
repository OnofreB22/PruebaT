from rest_framework import serializers

from core.models import Estacion


class EstacionSerializer(serializers.ModelSerializer):
    """Serializer para estaciones"""

    class Meta:
        model = Estacion
        fields = ['id', 'nombre', 'ubicacion']
        read_only_fields = ['id']

    def create(self, validated_data):
        estacion = Estacion(**validated_data)
        estacion.clean()
        estacion.save()
        return estacion
