from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxLengthValidator
from django.db import models


class SeoModel(models.Model):
    seo_title = models.CharField(
        verbose_name=_('SEO title'),
        max_length=70,
        blank=True,
        null=True,
        validators=[MaxLengthValidator(70)]
    )
    seo_description = models.TextField(
        verbose_name=_('SEO description'),
        max_length=300,
        blank=True,
        null=True,
        validators=[MaxLengthValidator(300)]
    )

    class Meta:
        abstract = True
