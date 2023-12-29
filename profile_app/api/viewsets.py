from rest_framework import viewsets 
from profile_app.api import serializers
from profile_app import models

class UserViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
