from django.contrib.auth import authenticate, logout, login
from django.http import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import *


# Список всех пользователей
class UsersList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]  # ИЗМЕНИТЬ ТОЛЬКО ДЛЯ АДМИНА!!!!


# Список всех рофилей
class ProfilesList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]  # ИЗМЕНИТЬ ТОЛЬКО ДЛЯ АДМИНА!!!!


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


class LogInView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return JsonResponse({'detail': 'Данные не были предоставлены'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'status': 'success', 'username': user.username}, status=status.HTTP_200_OK)
        return JsonResponse({'detail': 'Неверные учетные данные'}, status=status.HTTP_400_BAD_REQUEST)


class LogOutView(APIView):
    def post(self, request):
        logout(request)
        return JsonResponse({'status': 'success'}, status=status.HTTP_200_OK)


class CheckAuthView(APIView):
    permission_classes = [IsAuthenticated]  # Только для аутентифицированных пользователей


    def get(self, request):
        response = JsonResponse({'status': 'success', 'username': request.user.username}, status=200)
        response["Access-Control-Allow-Credentials"] = "true"
        return response


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
