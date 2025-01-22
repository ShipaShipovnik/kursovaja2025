from rest_framework import serializers
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'age','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            age=validated_data.get('age'),
            password=validated_data['password']
        )
        return user  # Возвращаем созданный объект пользователя

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class ProfileSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'profile_name', 'profile_bio', 'profile_spec', 'created_at', 'contacts', 'is_owner']

    def get_is_owner(self, obj):
        # Получаем флаг is_owner из контекста чтоб знать что профиль наш\не наш
        return self.context.get('is_owner', False)

