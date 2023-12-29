from rest_framework import serializers
from pacientes_app.models import Paciente

class PacientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'