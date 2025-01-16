from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from server import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/services/', include('services.urls')),
    path('api-auth/', include('rest_framework.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)