from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView

from .models import *
from .serializers import *


# УСЛУГИ
class ServicesList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]  # смотреть услуги могут все


class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]  # Только аутентифицированные пользователи могут добавлять услуги

    def perform_create(self, serializer):
        # автоматически устанавливаем автора услуги как текущего пользователя
        serializer.save(author=self.request.user)


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()


# КАТЕГОРИИ
class CategoriesList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]  # смотреть услуги могут все


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]  # Только аутентифицированные пользователи могут добавлять услуги


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_destroy(self, instance):
        instance.delete()
