from django.urls import path
from notifications_app.api import viewsets

urlpatterns = [
    path('notifications-list/', viewsets.ReceiveNotificationViewSets.as_view({'get': 'list'}), name='notifications-list'),
    path('receive_notification/', viewsets.ReceiveNotificationViewSets.as_view({'get': 'list', 'post': 'create'}), name='receive-notification'),
    
    path('notifications/<int:pk>/', viewsets.ReceiveNotificationViewSets.as_view({'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'}), name='notifications-detail'),
]
