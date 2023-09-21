from rest_framework import serializers
from .models import HistorialCodigo

class HistorialCodigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialCodigo
        fields = ('codigo', 'usuario', 'fecha_canje')