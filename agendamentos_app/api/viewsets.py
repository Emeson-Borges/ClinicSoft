from rest_framework import viewsets
from agendamentos_app.models import Agendamentos
from .serializers import AgendamentosSerializers
from agendamentos_app.models import Agendamentos
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# class AgendamentosViewSet(viewsets.ModelViewSet):
#     queryset = Agendamentos.objects.all()
#     serializer_class = AgendamentosSerializers
    
class AgendamentosViewSet(viewsets.ViewSet):
    # Listar agendamentos (GET)
    def list(self, request):
        queryset = Agendamentos.objects.all()
        serializer = AgendamentosSerializers(queryset, many=True)
        return Response(serializer.data)

    # Criar um novo agendamento (POST)
    def create(self, request):
        serializer = AgendamentosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
