from django.urls import path

from users.views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    # логин нужно
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/<int:profile_id>/', ProfileDetailView.as_view(), name='profile-details'),
    path('users-list/', UsersList.as_view(), name='users-list'),
    path('profiles-list/', ProfilesList.as_view(), name='profiles-list'),
]
