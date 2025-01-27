from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import CustomUser
from .models import *
from .serializers import *


# УСЛУГИ
class ServicesList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]  # смотреть услуги могут все


class MyServicesList(generics.ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]  # смотреть услуги могут все

    def get_queryset(self):
        return Service.objects.filter(author=self.request.user)


class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]  # Только аутентифицированные пользователи

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Автоматически назначаем автора


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()


# КАТЕГОРИИ
class CategoriesList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


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
