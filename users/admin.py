from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone', 'cpf', 'sexo', 'idade']

admin.site.register(CustomUser, CustomUserAdmin)
