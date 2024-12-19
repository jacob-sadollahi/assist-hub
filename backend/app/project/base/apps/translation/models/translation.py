from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class Translation(TimeStampedModel):
    key = models.CharField(
        verbose_name=_('key'),
        max_length=50,
        unique=True,
    )
    value = models.TextField(
        verbose_name=_('value'),
        blank=True,
    )

    class Meta:
        ordering = ('key',)
        verbose_name = _('translation')
        verbose_name_plural = _('translations')

    def __str__(self) -> str:
        return self.key
