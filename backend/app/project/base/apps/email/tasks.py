from django.core.mail import EmailMessage
from django.utils.safestring import mark_safe

from smtplib import SMTPRecipientsRefused, SMTPServerDisconnected

from project import celery_app
from project.base.apps.core.tasks import BaseTask
from project.base.apps.email.models.email import Email


class SendMailTask(BaseTask):
    name = 'project.base.apps.email.tasks.SendMailTask'
    description = 'Send Mails'
    max_retries = 3
    throws = (SMTPRecipientsRefused, SMTPServerDisconnected)

    @staticmethod
    def get_email(**kwargs):
        return Email.objects.get(pk=kwargs.get('pk'))

    def _run(self, *args, **kwargs):
        email = self.get_email(**kwargs)
        self.logger.info(f'Processing mail for {email.to}')
        try:
            message = EmailMessage(
                subject=email.subject,
                body=mark_safe(email.compiled_template),
                to=email.to.split(','),
                bcc=email.bcc.split(',')
            )
            message.content_subtype = 'html'
            for attach in email.attachments.all():
                message.attach(*attach.attach_args)
            message.send()
            email.is_sent = True
            email.save(update_fields=['is_sent'])
            self.logger.info('Mail sent!')
        except (SMTPRecipientsRefused, SMTPServerDisconnected) as e:
            self.logger.warning('{0!r} failed: {1!r}'.format(self.request.id, e))
            email.error = str(e)
            email.save(update_fields=['error'])
            self.retry(countdown=10, exc=e)


send_mail_task = SendMailTask()
celery_app.register_task(send_mail_task)
