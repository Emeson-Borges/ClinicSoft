from django.urls import path
from agendamentos_app.api import viewsets

app_name = 'agendamentos_app'

urlpatterns = [
    path('agendamentos/', viewsets.AgendamentosViewSet.as_view({'get': 'list'}), name='agendamentos-list'),
    path('agendamentos-create/', viewsets.AgendamentosViewSet.as_view({'get': 'list', 'post': 'create'}), name='agendamentos-list-create'),

    path('agendamentos/<int:pk>/', viewsets.AgendamentosViewSet.as_view({'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'}), name='agendamentos-detail'),
]
