from django.urls import path
from .views import *

urlpatterns = [
    path('services-list/', ServicesList.as_view(), name='services-list'),
    path('services-list/', CategoriesList.as_view(), name='categories-list'),
    path('services/create/', ServiceCreateView.as_view(), name= 'add-service'),
    path('services/update/', ServiceCreateView.as_view(), name='add-edit'),
    path('services/create/', ServiceCreateView.as_view(), name='add-service')

]
