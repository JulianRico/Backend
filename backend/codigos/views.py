from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Codigo
from promociones.models import Promocion
from .serializers import CodigoSerializer
from datetime import datetime, timedelta
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
import pytz

class GenerarCodigoView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, idPromocion, format=None):
        # Generar un nuevo código con el nombre de usuario
        try:
            promocion = Promocion.objects.get(pk=idPromocion)
        except Promocion.DoesNotExist:
            return Response({"error": "La promoción no existe."}, status=status.HTTP_404_NOT_FOUND)

        print(request.user.username)
        # Capturar el nombre de usuario del usuario autenticado
        username = 'julian' if request.user.username is None else 'pepito'

        # Verificar si ya existe un código para esta promoción y usuario
        codigo_existente = Codigo.objects.filter(idPromocion=idPromocion, username=username).first()

        if codigo_existente:
            return Response({"error": "El usuario ya tiene un código para esta promoción.", "codigo":f"{codigo_existente}"}, status=status.HTTP_400_BAD_REQUEST)

        nuevo_codigo = Codigo(idPromocion=idPromocion,  username="pepito")
        nuevo_codigo.save()

        serializer = CodigoSerializer(nuevo_codigo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
