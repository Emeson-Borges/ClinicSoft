from django.contrib.auth.models import AbstractUser,  Group, Permission
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=15, unique=True, blank=True, null=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    USERNAME_FIELD = 'cpf'
    
    class Meta:
        db_table = 'profile_user'
        managed = True
        verbose_name = 'ProfileUser'
        verbose_name_plural = 'ProfileUsers'
        
    def __str__(self):
        return self.user.username
