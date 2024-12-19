import uuid

from django.db import models
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel


class Email(TimeStampedModel):
    to = models.TextField(
        verbose_name='To',
    )
    subject = models.CharField(
        verbose_name='Subject',
        max_length=200,
    )
    compiled_template = models.TextField(
        verbose_name='compiled_template',
        blank=True,
    )
    bcc = models.TextField(
        verbose_name='bcc',
        blank=True,
    )
    is_sent = models.BooleanField(
        verbose_name='is_sent',
        default=False,
    )
    error = models.TextField(
        verbose_name='error',
        null=True,
        blank=True,
    )
    token = models.UUIDField(
        verbose_name='token',
        unique=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return f'{self.subject} -> {self.to}'

    def get_absolute_url(self):
        return reverse('email:emails-detail-view', kwargs={'pk': self.pk})
