from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinLengthValidator, MaxLengthValidator
from PIL import Image
import os

from services.utils import service_photo_path


class Service(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=300)
    descr = models.TextField()
    priceMin = models.FloatField(null=False, blank=False)
    priceMax = models.FloatField(null=True, blank=True)
    photos = models.JSONField(default=list)
    isActive = models.BooleanField(default=True)
    amount = models.PositiveIntegerField(null=True, blank=False)
    workTime = models.CharField(max_length=150)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='services')

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

    def create_thumbnails(self):
        for photo in self.photos:
            img_path = photo.path
            img = Image.open(img_path)
            width, height = img.size

            # миниатюра
            size = min(width, height)
            left = (width - size) / 2
            top = (height - size) / 2
            right = (width + size) / 2
            bottom = (height + size) / 2

            img = img.crop((left, top, right, bottom))
            img.thumbnail((200, 200))

            # Сохраняем миниатюру
            thumbnail_path = os.path.splitext(img_path)[0] + '_thumbnail.jpg'
            img.save(thumbnail_path, 'JPEG')

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
