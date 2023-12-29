from django.urls import path
from agendamentos_app.api import viewsets

app_name = 'agendamentos_app'

urlpatterns = [
    path('agendamentos/', viewsets.AgendamentosViewSet.as_view({'get': 'list'}), name='agendamentos-list'),
    path('agendamentos-create/', viewsets.AgendamentosViewSet.as_view({'get': 'list', 'post': 'create'}), name='agendamentos-list-create'),
]
