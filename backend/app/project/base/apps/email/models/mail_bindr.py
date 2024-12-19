import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class MailBindr(TimeStampedModel):
    id = models.UUIDField(
        verbose_name=_('ID'),
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    to = models.TextField(
        verbose_name=_('To'),
    )
    variables = models.JSONField(
        verbose_name=_('Variables'),
        null=True,
        blank=True,
    )
    bcc = models.TextField(
        verbose_name=_('bcc'),
        blank=True,
    )
    is_sent = models.BooleanField(
        verbose_name=_('Is sent'),
        default=False,
    )
    response = models.TextField(
        verbose_name=_('response'),
        null=True,
        blank=True,
    )
    error = models.TextField(
        verbose_name=_('Error'),
        null=True,
        blank=True,
    )
    html_body = models.TextField(
        verbose_name=_('html body'),
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Mail Binder')
        verbose_name_plural = _('Mail Binders')

    def __str__(self) -> str:
        return str(self.to)

    def get_absolute_url(self):
        return reverse('email:mailbindr-html-view', kwargs={'pk': self.pk})
