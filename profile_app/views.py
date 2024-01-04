from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from knox.auth import AuthToken
from django.utils import timezone
from datetime import timedelta
from rest_framework import viewsets
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    token_expires = refresh.access_token.payload['exp']
    
    profile_data = {}
    if hasattr(user, 'ProfileUser'):
        profile_data = {
            'phone': user.ProfileUser.phone,
            'cpf': user.ProfileUser.cpf,
        }

    return Response({
        'user_info': {
            'id': user.id,
            'name': user.username,
            'email': user.email,
            'token_expires': token_expires,
            **profile_data,
        },
        # 'token': token
        'token': access_token,
    })


@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        profile_data = {}
        if hasattr(user, 'ProfileUser'):
            profile_data = {
                'phone': user.ProfileUser.phone,
                'cpf': user.ProfileUser.cpf,
            }

        return Response({
            'user_info': {
                'id': user.id,
                'name': user.username,
                'email': user.email,
                **profile_data,
            }
        })

    return Response({'error': 'not authenticated'}, status=400)