from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from rest_framework import viewsets

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)

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
        },
        'token': token
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