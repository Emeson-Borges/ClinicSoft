from rest_framework import viewsets
from medicos_app.models import Medicos
from .serializers import MedicosSerializers
from rest_framework.response import Response
from rest_framework import status

class MedicosViewSet(viewsets.ModelViewSet):
    queryset = Medicos.objects.all()  # Defina seu conjunto de dados aqui
    serializer_class = MedicosSerializers
    # Listar Medicos (GET)
    def list(self, request):
        queryset = Medicos.objects.all()
        serializer = MedicosSerializers(queryset, many=True)
        return Response(serializer.data)

    # Criar um novo Medico (POST)
    def create(self, request):
        serializer = MedicosSerializers(data=request.data)
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