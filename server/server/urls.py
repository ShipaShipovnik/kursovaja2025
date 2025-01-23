from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from server import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/services/', include('services.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # JWT-аутентификация
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Получение токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновление токена
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Проверка токена
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
