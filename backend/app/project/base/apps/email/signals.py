from django.db.models.signals import post_save

from project.base.apps.email.models import Email
from project.base.apps.email.tasks import send_mail_task


class MailSignal:
    @staticmethod
    def send_mail(sender, instance, created, **kwargs):
        if not instance.is_sent and not instance.error:
            send_mail_task.delay(pk=instance.pk)


post_save.connect(MailSignal.send_mail, sender=Email)
