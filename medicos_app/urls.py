from django.urls import path
from medicos_app.api import viewsets

app_name = 'medicos_app'

urlpatterns = [
    path('medicos/', viewsets.MedicosViewSet.as_view({'get': 'list'}), name='medicos-list'),
    path('medicos-create/', viewsets.MedicosViewSet.as_view({'get': 'list', 'post': 'create'}), name='medicos-list-create'),
]