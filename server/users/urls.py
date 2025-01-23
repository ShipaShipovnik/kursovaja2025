from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import *

urlpatterns = [
    # Регистрация и профили
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('my-user/', CurrentUserView.as_view(), name='current-user'),
    path('my-profile/', CurrentProfileView.as_view(), name='current-user-profile'),
    path('profile/<int:profile_id>/', ProfileDetailView.as_view(), name='profile-details'),
    # Списки пользователей и профилей
    path('users-list/', UsersList.as_view(), name='users-list'),
    path('profiles-list/', ProfilesList.as_view(), name='profiles-list'),
]
