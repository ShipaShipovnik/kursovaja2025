from rest_framework import serializers
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'age', 'password']
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
        return user


# Серилизатор профиля
class ProfileSerializer(serializers.ModelSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'profile_name', 'profile_bio', 'profile_spec', 'created_at', 'contacts', 'is_owner']

    def get_is_owner(self, obj):
        # Получаем флаг is_owner из контекста
        return self.context.get('is_owner', False)

    def validate_contacts(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Contacts must be a JSON object.")
        return value
