from rest_framework import serializers
from agendamentos_app.models import Agendamentos

class AgendamentosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Agendamentos
        fields = '__all__'