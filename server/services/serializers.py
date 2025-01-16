from rest_framework import serializers
from .models import *


# Услуги
class ServiceSerializer(serializers.ModelSerializer):
    photos = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        validators=[MinLengthValidator(1), MaxLengthValidator(5)]
    )

    class Meta:
        model = Service
        fields = ['id', 'title', 'descr', 'priceMax', 'photos', 'isActive', 'amount', 'workTime', 'category']

    def create(self, validated_data):
        photos = validated_data.pop('photos')
        service = Service.objects.create(**validated_data)

        for photo in photos:
            service.photos.append(photo)

        service.create_thumbnails()

        service.save()
        return service


# Категории
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
