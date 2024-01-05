from django.contrib import admin
from django.urls import include, path
from knox import views as knox_views
from rest_framework import routers

from agendamentos_app.urls import urlpatterns as agendamentos_urls
from pacientes_app.urls import urlpatterns as pacientes_urls
from medicos_app.urls import urlpatterns as medicos_urls
from notifications_app.urls import urlpatterns as notifications_urls

route = routers.DefaultRouter()

#route.register(r'users', viewsets.UserViewset, basename='Users')
# route.register(r'pacientes', viewsets.PacientesViewSet, basename='pacientes')
# route.register(r'agendamentos', viewsets.AgendamentosViewSet, basename='agendamentos')

urlpatterns = [
    #Rotas de Login
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    
    path('api/', include(route.urls)),
    path('api/', include(agendamentos_urls)),
    path('api/', include(pacientes_urls)),
    path('api/', include(medicos_urls)),
    path('api/', include(notifications_urls)),
]

