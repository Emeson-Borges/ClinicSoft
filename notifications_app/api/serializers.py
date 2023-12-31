from rest_framework import serializers
from notifications_app.models import Notification

class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'remetente', 'message', 'lida']
