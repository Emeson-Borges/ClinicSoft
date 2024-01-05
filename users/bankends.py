# users/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CPFBackend(ModelBackend):
    def authenticate(self, request, cpf=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(cpf=cpf)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None
