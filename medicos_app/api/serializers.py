from rest_framework import serializers
from medicos_app.models import Medicos

class MedicosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medicos
        fields = '__all__'
    