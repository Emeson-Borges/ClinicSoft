# users/views.py
from django.contrib.auth import authenticate, get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        cpf = request.data.get('cpf')
        password = request.data.get('password')

        if cpf is None or password is None:
            return Response({'error': 'Por favor, forneça CPF e senha.'}, status=400)

        user = authenticate(request, cpf=cpf, password=password)

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

        return Response({'non_field_errors': ['Impossível fazer login com as credenciais fornecidas.']}, status=400)
    
    @action(detail=False, methods=['get'])
    def user_list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
    
    def user_create(self, request, *args, **kwargs):
        if request.method == 'GET':
            # Handle GET requests
            # For example, you might want to retrieve a list of users
            users = CustomUser.objects.all()
            serializer = CustomUser(users, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            # Handle POST requests
            # For example, you might want to create a new user
            serializer = CustomUser(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        else:
            # Handle other HTTP methods if needed
            return Response({'error': 'Method not allowed'}, status=405)
