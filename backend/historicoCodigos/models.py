from django.db import models
from django.contrib.auth.models import User

class HistorialCodigo(models.Model):
    codigo = models.CharField(max_length=20)
    usuario = models.CharField(max_length=8, unique=True, editable=False)
    fecha_canje = models.DateTimeField(auto_now_add=True)