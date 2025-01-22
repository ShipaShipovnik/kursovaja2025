from django.contrib.auth.views import LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users.views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('check-auth/', CheckAuthView.as_view(), name='check-auth'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/<int:profile_id>/', ProfileDetailView.as_view(), name='profile-details'),
    path('users-list/', UsersList.as_view(), name='users-list'),
    path('profiles-list/', ProfilesList.as_view(), name='profiles-list'),
]
