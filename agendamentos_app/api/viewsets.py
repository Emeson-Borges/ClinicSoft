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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)