from django.db import models
import uuid
from datetime import datetime, timedelta
from django.contrib.auth.models import User  # Importa el modelo de usuario si no está importado

class Codigo(models.Model):
    idPromocion = models.CharField(max_length=20)
    codigo = models.CharField(max_length=8, unique=True, editable=False)  # Cambiado a CharField para el código    
    username = models.CharField(max_length=255)  # Campo para almacenar el nombre de usuario

    def __str__(self):
        return self.codigo

    def save(self, *args, **kwargs):
        # Generar un nuevo UUID y truncarlo a 8 caracteres si el código no existe
        if not self.codigo:
            new_uuid = uuid.uuid4()
            self.codigo = str(new_uuid)[:8]
        super().save(*args, **kwargs)  # Llamar al método save() de la clase base para guardar el objeto