from django.urls import path
from .views import *

urlpatterns = [
    # улсуги
    path('services-list/', ServicesList.as_view(), name='services-list'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('create/', ServiceCreateView.as_view(), name= 'add-service'),
    # категории
    path('categories-list/', CategoriesList.as_view(), name='categories-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/create/', CategoryCreateView.as_view(), name='add-category'),
]
