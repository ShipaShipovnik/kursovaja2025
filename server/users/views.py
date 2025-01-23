from django.contrib.auth import logout, authenticate, login
from rest_framework import status, generics, permissions
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import CustomUser, Profile
from .serializers import CustomUserSerializer, ProfileSerializer


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


# Регистрация
class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Возвращаем данные пользователя
        return Response({
            'user': user_serializer.data,
        }, status=status.HTTP_201_CREATED)


# Вход
# class LogInView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response({'detail': 'Неверные данные'}, status=status.HTTP_400_BAD_REQUEST)
#
#         username = serializer.validated_data['username']
#         password = serializer.validated_data['password']
#
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             user_data = CustomUserSerializer(user).data
#             return Response({'status': 'success', 'user': user_data}, status=status.HTTP_200_OK)
#         return Response({'detail': 'Неверные учетные данные'}, status=status.HTTP_400_BAD_REQUEST)
#
#
# # Выход
# class LogOutView(APIView):
#     def post(self, request):
#         logout(request)
#         request.session.flush()
#         return Response({'status': 'success'}, status=status.HTTP_200_OK)
#
#
# # Проверка аутентификации
# class CheckAuthView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get(self, request):
#         user_data = CustomUserSerializer(request.user).data
#         return Response({'status': 'success', 'user': user_data}, status=status.HTTP_200_OK)


# Возвращает профиль текущего пользователя
class CurrentProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        try:
            return self.request.user.profile
        except Profile.DoesNotExist:
            raise NotFound("Profile not found.")


# Возвращает текущего пользователя
class CurrentUserView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# Получение и обновление профиля
class ProfileDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        profile_id = self.kwargs.get('profile_id')
        profile = get_object_or_404(Profile, id=profile_id)
        return profile

    def get_serializer_context(self):
        context = super().get_serializer_context()
        profile = self.get_object()
        context['is_owner'] = self.request.user.is_authenticated and self.request.user == profile.user
        return context
