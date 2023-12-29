from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import ProfileUser

class UsernameCPFBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(profileuser__cpf=username)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
