from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'  # Указываем имя приложения
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        from users import signals
