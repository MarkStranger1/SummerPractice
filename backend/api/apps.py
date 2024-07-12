from django.apps import AppConfig

"""
Определяем API конфигурацию приложения Django
"""


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
