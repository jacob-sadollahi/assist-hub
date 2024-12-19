from django.apps import AppConfig
from project.settings import _


class UserConfig(AppConfig):
    name = 'project.base.apps.user'
    verbose_name = _('Manage admin users')
    label = 'user'

    def ready(self):
        from .signals import create_user_profile  # noqa
