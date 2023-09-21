from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  HistorialCodigo
from codigos.models import Codigo
from datetime import datetime
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny

class CanjearCodigoView(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [AllowAny]

    def post(self, request, codigo_id, format=None):
        try:
            print(codigo_id)
            codigo = Codigo.objects.get(codigo=codigo_id)
            print(codigo)
        except Codigo.DoesNotExist:
            return Response({"error": "El código no existe."}, status=status.HTTP_404_NOT_FOUND)

        if HistorialCodigo.objects.filter(codigo=codigo_id, usuario='pepito').exists():
            return Response({"error": "El código ya ha sido canjeado por este usuario."}, status=status.HTTP_400_BAD_REQUEST)

        # Registrar el canje en el historial
        historial = HistorialCodigo(codigo=codigo_id, usuario='pepito')
        historial.save()

        return Response({"message": "Código canjeado con éxito."}, status=status.HTTP_201_CREATED)
