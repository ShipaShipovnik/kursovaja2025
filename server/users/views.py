from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

from .serializers import *

#Список всех пользователей
class UsersList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny] #ИЗМЕНИТЬ ТОЛЬКО ДЛЯ АДМИНА!!!!

#Список всех рофилей
class ProfilesList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny] #ИЗМЕНИТЬ ТОЛЬКО ДЛЯ АДМИНА!!!!

#
class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]  # можно всем

    def create(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        profile_data = request.data.get('profile', None)
        if profile_data:
            profile_serializer = ProfileSerializer(data=profile_data)
            profile_serializer.is_valid(raise_exception=True)
            profile_serializer.save(user=user)

        return Response(user_serializer.data, status=status.HTTP_201_CREATED)


# данные пользователя
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user  # Возвращает пользоваеля


# Получение и обновление профиля
class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]  # Разрешаем смотреть всем

    def get_object(self):
        profile_id = self.kwargs.get('profile_id')
        profile = get_object_or_404(Profile, id=profile_id)
        return profile

    def get_serializer_context(self):
        # Добавляем флаг is_owner в контекст
        context = super().get_serializer_context()
        profile = self.get_object()
        context['is_owner'] = self.request.user.is_authenticated and self.request.user == profile.user
        return context
