# users/views.py
from django.contrib.auth import authenticate, get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.token_blacklist.models import RefreshToken as RefreshTokenModel
from knox.auth import AuthToken

from .models import CustomUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Por favor, forneça CPF e senha.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            token_expires = refresh.access_token.payload['exp']

            return Response({
                'user_info': {
                    'id': user.id,
                    'name': user.username,
                    'email': user.email,
                    'token_expires': token_expires,
                },
                'token': access_token,
            })

        return Response({'non_field_errors': ['Impossível fazer login com as credenciais fornecidas.']}, status=status.HTTP_400_BAD_REQUEST)
   
    @action(detail=False, methods=['get'])
    def user_list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
    
    def user_create(self, request, *args, **kwargs):
        if request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)