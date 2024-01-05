from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

# urlpatterns = router.urls

urlpatterns = [
    path('login/', UserViewSet.as_view({'post': 'login'}), name='user-login'),
    path('user_create/', UserViewSet.as_view({'post': 'user_create'}), name='user-create'),
    path('user-list/', UserViewSet.as_view({'get': 'user_list'}), name='user-list'),
]