from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    default_app_config = ''
    name = 'app'

    def ready(self):
        import app.signals