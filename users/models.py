# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    sexo = models.CharField(max_length=1)
    idade = models.PositiveIntegerField()
    password = models.CharField(max_length=128)
    
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['email', 'phone', 'sexo', 'idade']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        managed = True
        verbose_name = 'user'
        verbose_name_plural = 'users'