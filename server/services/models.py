from django.conf import settings
from django.db import models


class Service(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=300)
    descr = models.TextField()
    priceMin = models.FloatField(null=False, blank=False)
    priceMax = models.FloatField(null=True, blank=True)
    # photos = models.JSONField(default=list)
    isActive = models.BooleanField(default=True)
    amount = models.PositiveIntegerField(null=True,blank=False)
    workTime = models.CharField(max_length=150)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='services')


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