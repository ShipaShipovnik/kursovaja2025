from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)

    first_name = None
    last_name = None

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    profile_name = models.CharField(max_length=100, blank=True, null=True)
    profile_bio = models.TextField(blank=True, null=True)
    profile_spec = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    contacts = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Профиль {self.profile_name}"


# Сигнал для автоматического создания профиля при регистрации пользователя
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(
            user=instance,
            defaults={
                'profile_name': instance.username,  # имя профиля по умолчанию
                'profile_bio': 'Расскажите о себе',  # bio по умолчанию
            }
        )
