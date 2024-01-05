# users/views.py
from django.contrib.auth import authenticate, get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    # @action(detail=False, methods=['post'])
    # def login(self, request):
    #     username = request.data.get('cpf')  # Login usando username=cpf
    #     password = request.data.get('password')

    #     user = authenticate(request, username=username, password=password)

    #     if user is not None:
    #         refresh = RefreshToken.for_user(user)
    #         access_token = str(refresh.access_token)
    #         token_expires = refresh.access_token.payload['exp']

    #         return Response({
    #             'user_info': {
    #                 'id': user.id,
    #                 'name': user.username,
    #                 'email': user.email,
    #                 'token_expires': token_expires,
    #             },
    #             'token': access_token,
    #         })
    #     else:
    #         return Response({'non_field_errors': ['Impossível fazer login com as credenciais fornecidas.']}, status=400)

    # @action(detail=False, methods=['post'])
    # def user_create(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)

    #     # Adicione o campo de senha ao retorno
    #     response_data = serializer.data
    #     response_data['password'] = '********'  # Adapte conforme necessário

    #     headers = self.get_success_headers(serializer.data)

    #     return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


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
