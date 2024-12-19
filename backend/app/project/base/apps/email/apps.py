from django.apps import AppConfig


class EmailConfig(AppConfig):
    name = 'project.base.apps.email'

    def ready(self):
        from project.base.apps.email.signals import MailSignal  # noqa