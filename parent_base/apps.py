from django.apps import AppConfig


class ParentBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'parent_base'
