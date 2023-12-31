from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from notifications_app.models import Notification
from notifications_app.api.serializers import NotificationSerializers


class ReceiveNotificationViewSets(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializers
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = NotificationSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Notification.objects.all()
        serializer = NotificationSerializers(queryset, many=True)
        return Response(serializer.data)