from datetime import timedelta
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework.generics import RetrieveUpdateAPIView

class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]


class TokenRenewView(APIView):    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Obtener el token actual del usuario autenticado
        
        token, created = Token.objects.get_or_create(user=request.user)
        
        # Actualizar la fecha de vencimiento del token
        # Verifica si el token aún es válido
        if token.created < timezone.now() - timedelta(days=30):
            return Response({'detail': 'Token no válido'}, status=status.HTTP_400_BAD_REQUEST)

        # Genera un nuevo token
        token.delete()  # Elimina el token actual
        new_token = Token.objects.create(user=request.user)

        return Response({'token': new_token.key})
    
class UserDetailsView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        return self.request.user
    
class UpdateUserView(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user