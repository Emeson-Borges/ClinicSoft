from rest_framework import viewsets
from pacientes_app.models import Paciente
from .serializers import PacientesSerializers
from rest_framework.response import Response
from rest_framework import status

class PacientesViewSet(viewsets.ViewSet):
    # Listar agendamentos (GET)
    def list(self, request):
        queryset = Paciente.objects.all()
        serializer = PacientesSerializers(queryset, many=True)
        return Response(serializer.data)

    # Criar um novo agendamento (POST)
    def create(self, request):
        serializer = PacientesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
