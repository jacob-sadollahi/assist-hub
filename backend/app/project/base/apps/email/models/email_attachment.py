import mimetypes
from typing import Tuple

from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class EmailAttachment(TimeStampedModel):
    email = models.ForeignKey(
        verbose_name=_('email'),
        to='email.Email',
        on_delete=models.CASCADE,
        related_name='attachments'
    )
    file = models.FileField(
        verbose_name=_('file'),
        upload_to='emails/attachments'
    )

    class Meta:
        verbose_name = _('Email attachment')
        verbose_name_plural = _('Email Attachments')

    def __str__(self) -> str:
        return f'{self.email}'

    @property
    def attach_args(self) -> Tuple:
        return (
            self.file.name, self.file.read(), mimetypes.guess_type(self.file.path)[0]
        )
