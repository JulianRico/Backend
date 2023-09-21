import uuid
from django.db import models

class Promocion(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion_larga = models.TextField()
    imagenes = models.JSONField()
    porcentaje_descuento = models.DecimalField(max_digits=5, decimal_places=2)
    precio_estandar = models.DecimalField(max_digits=10, decimal_places=2)    
    codigo = models.CharField(max_length=8, unique=True, editable=False)
    fecha_inicial = models.DateTimeField()
    fecha_finalizacion = models.DateTimeField()
    
    def __str__(self):
        return self.titulo
    
    @property
    def precio_con_descuento(self):
        return self.precio_estandar - (self.precio_estandar * (self.porcentaje_descuento / 100))
    
    def save(self, *args, **kwargs):
        # Generar un nuevo UUID y truncarlo a 8 caracteres
        if not self.codigo:
            while True:
                new_uuid = uuid.uuid4()
                new_codigo = str(new_uuid)[:8]
                # Verificar si el nuevo código ya existe en la base de datos
                if not Promocion.objects.filter(codigo=new_codigo).exists():
                    self.codigo = new_codigo
                    break

        super().save(*args, **kwargs)