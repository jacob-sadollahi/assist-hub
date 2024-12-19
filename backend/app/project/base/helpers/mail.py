from typing import List, Dict

from django.http import HttpRequest
from django.template.loader import render_to_string
from django.conf import settings

from project.base.apps.email.models import Email


class BaseMail:
    description: str
    from_email: str
    context: Dict = {}
    bcc: List = []
    template_name: str = 'mail_base.html'
    from_email: str = settings.DEFAULT_FROM_EMAIL

    def __init__(
            self,
            to: List,
            request: HttpRequest,
            email_subject: str,
            context: Dict = None,
            description: str = None,
            template_name: str = None,
            bcc: List = None,
            from_email: str = None
    ):
        self.to = to
        self.request = request
        if from_email:
            self.from_email = from_email
        if bcc:
            self.bcc = bcc
        if context:
            self.context = context
        if description:
            self.description = description
        if template_name:
            self.template_name = template_name
        if email_subject:
            self.email_subject = email_subject
        else:
            self.email_subject = 'An error occurred'

    def create_email(self):
        self.context.update({
            'title': self.email_subject,
            'description': self.description,
        })
        body = render_to_string(
            template_name=self.template_name,
            context=self.context,
            request=self.request,
        )
        email = Email(
            to=','.join(self.to),
            subject=self.email_subject,
            compiled_template=body,
            bcc=','.join(self.bcc),
        )
        if self.from_email:
            email.from_email = self.from_email
        email.save()
        return email

    def send(self):
        return self.create_email()


class AdminMail(BaseMail):
    to = [a[1] for a in settings.ADMINS]

    def __init__(self, request, email_subject):
        super().__init__(self.to, request, email_subject)
