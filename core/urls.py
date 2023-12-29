from profile_app.api import viewsets
from profile_app.views import get_user_data, login_api
from django.contrib import admin
from django.urls import include, path
from knox import views as knox_views
from rest_framework import routers

route = routers.DefaultRouter()

route.register(r'users', viewsets.UserViewset, basename='Users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',  login_api),
    path('user_data/',  get_user_data),
    path('logout/',  knox_views.LogoutView.as_view()),
    path('logout_all/',  knox_views.LogoutAllView.as_view()),
    path('', include(route.urls))
]