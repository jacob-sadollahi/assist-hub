from django.db import models
from django.utils import timezone

from project.settings import _

from project.base.apps.core.enums import StatusEnum


class StatusQuerySet(models.QuerySet):

    def published(self):
        return self.filter(status=StatusEnum.PUBLISH)

    def draft(self):
        return self.filter(status=StatusEnum.DRAFT)


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def draft(self):
        return self.get_queryset().draft()


class StatusModel(models.Model):
    status = models.CharField(
        verbose_name=_("status"),
        max_length=30,
        choices=StatusEnum.CHOICES,
        default=StatusEnum.DRAFT,
    )
    published_date = models.DateTimeField(
        verbose_name=_("published date"),
        blank=True,
        null=True,
        editable=False,
    )
    drafted_date = models.DateTimeField(
        verbose_name=_("drafted date"),
        blank=True,
        null=True,
        editable=False,
    )
    objects = StatusManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.status == StatusEnum.PUBLISH:
            self.published_date = timezone.now()

        if self.status == StatusEnum.DRAFT:
            self.drafted_date = timezone.now()

        return super().save(*args, **kwargs)
