from django.urls import path
from .api import viewsets

app_name = 'pacientes_app'

urlpatterns = [
    path('pacientes/', viewsets.PacientesViewSet.as_view({'get': 'list'}), name='pacientes-list'),
    path('pacientes-create/', viewsets.PacientesViewSet.as_view({'get': 'list', 'post': 'create'}), name='pacientes-list-create'),
    
    path('pacientes/<int:pk>/', viewsets.PacientesViewSet.as_view(
        {'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'}), name='pacientes-detail'),
]
