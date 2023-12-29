from django.contrib.auth.models import User
from knox.auth import AuthToken
from rest_framework import serializers, validators

from profile_app.models import ProfileUser


class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('cpf', 'phone')

class UserSerializer(serializers.ModelSerializer):
    ProfileUser = ProfileUserSerializer(required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'ProfileUser')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(),
                        'A user with that Email already exists'
                    )
                ]
            }
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('ProfileUser', {})
        user = User.objects.create(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        ProfileUser.objects.create(user=user, **profile_data)
        return user
