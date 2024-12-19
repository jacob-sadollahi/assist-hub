from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django_extensions.db.models import TimeStampedModel

from project.settings import LANGUAGES


class Profile(TimeStampedModel):
    user = models.OneToOneField(
        verbose_name=_("user"),
        to=settings.AUTH_USER_MODEL,
        related_name="profile",
        on_delete=models.CASCADE,
    )
    country = CountryField(
        verbose_name=_("country"),
        blank=True,
    )
    language = models.CharField(
        verbose_name=_("language"),
        max_length=5,
        choices=LANGUAGES,
        default="en",
        blank=True,
    )

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = _("User-Profile")
        verbose_name_plural = _("User-Profiles")
