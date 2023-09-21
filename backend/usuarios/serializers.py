from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'full_name','address', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'], 
            full_name=validated_data['full_name'],           
            address=validated_data.get('address', ''),
            phone_number=validated_data.get('phone_number', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        # Actualizar campos solo si se proporcionan en los datos validados
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)

        # Actualizar la contraseña si se proporciona
        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        # Guardar el usuario actualizado
        instance.save()
        return instance