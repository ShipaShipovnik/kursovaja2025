from tkinter import Image

from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinLengthValidator, MaxLengthValidator
import os
from .utils import service_photo_path


class Service(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=300)
    descr = models.TextField()
    priceMin = models.FloatField(null=False, blank=False)
    priceMax = models.FloatField(null=True, blank=True)
    # photo = models.CharField(max_length=500, null=True, blank=True)  # Путь к одному файлу
    isActive = models.BooleanField(default=True)
    amount = models.PositiveIntegerField(null=True, blank=False)
    workTime = models.CharField(max_length=150)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='services')

    def __str__(self):
        return f"{self.title} - {self.category_name} - {self.service_author}"

    @property
    def category_name(self):
        return self.category.name if self.category else "No Category"

    @property
    def service_author(self):
        if hasattr(self.author, 'profile'):
            return self.author.profile.profile_name
        return "No Profile"

    # def save_photo(self, photo):
    #     # Генерируем уникальное имя файла
    #     photo_name = f"{self.title}_{photo.name}"
    #     photo_path = os.path.join('services', photo_name)  # Путь для сохранения
    #     full_path = os.path.join(settings.MEDIA_ROOT, photo_path)
    #
    #     # Создаем директорию, если её нет
    #     os.makedirs(os.path.dirname(full_path), exist_ok=True)
    #
    #     # Сохраняем файл на сервере
    #     with open(full_path, 'wb+') as destination:
    #         for chunk in photo.chunks():
    #             destination.write(chunk)
    #
    #     # Сохраняем путь к файлу в базе данных
    #     self.photo = photo_path
    #     self.save()

    class Meta:
        verbose_name_plural = "Услуги"
        verbose_name = "Услуга"


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"
