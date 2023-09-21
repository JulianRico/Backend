from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Campos personalizados    
    full_name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)    
    long = models.CharField(max_length=50, blank=True)
    lati = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)

    # Otros campos heredados de AbstractUser
    # username, first_name, last_name, email, password, etc.
    class Meta:
        db_table = 'usuarios_customuser'
    def __str__(self):
        return self.username


