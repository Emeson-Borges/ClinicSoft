from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from pacientes_app.models import Paciente

from .serializers import PacientesSerializers


class PacientesViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacientesSerializers
    
    # Listar agendamentos (GET)
    def list(self, request):
        queryset = Paciente.objects.all()
        serializer = PacientesSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = get_object_or_404(self.queryset, pk=kwargs.get('pk'))
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request):
        serializer = PacientesSerializers(data=request.data)
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
    