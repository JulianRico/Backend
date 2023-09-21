from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Promocion
from .serializers import PromocionSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class PromocionListView(ListCreateAPIView):
    queryset = Promocion.objects.all().order_by('-fecha_finalizacion')
    serializer_class = PromocionSerializer

class EditPromocionView(RetrieveUpdateAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer    
    # Puedes agregar permisos de autenticación y acceso aquí si es necesario.

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        # Lista de campos que se pueden actualizar
        allowed_fields = ['titulo', 'descripcion_larga', 'imagenes', 'porcentaje_descuento', 'precio_estandar']

        # Eliminar campos no permitidos del diccionario de datos antes de la actualización
        for field in serializer.validated_data.copy():
            if field not in allowed_fields:
                del serializer.validated_data[field]

        # Realizar la actualización
        serializer.save()


class EliminarPromocionView(DestroyAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer
    permission_classes = [AllowAny]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "La promoción ha sido eliminada con éxito."}, status=status.HTTP_204_NO_CONTENT)