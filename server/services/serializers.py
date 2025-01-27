from tkinter import Image

from rest_framework import serializers
from .models import *


# Услуги
class ServiceSerializer(serializers.ModelSerializer):
    # photo = serializers.ImageField(
    #     write_only=True,
    #     required=True,
    # )

    class Meta:
        model = Service
        fields = ['id', 'title', 'descr', 'priceMin', 'priceMax', 'isActive', 'amount', 'workTime', 'category']

    def create(self, validated_data):
        # photo = validated_data.pop('photo')  # Извлекаем файл
        service = Service.objects.create(**validated_data)  # Создаем услугу
        # service.save_photo(photo)
        return service


# Категории
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
