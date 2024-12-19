from django.apps import AppConfig
from project.settings import _


class TranslationConfig(AppConfig):
    name = 'project.base.apps.translation'
    verbose_name = _('translation')
    label = 'translation'
