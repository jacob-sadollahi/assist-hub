from datetime import datetime, timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from project import settings
from project.base.helpers import code_generator
from ..managers import UserEmailManager


class Email(TimeStampedModel):
    """
    Used to allow multiple e-mail adresses for one user
    """
    expired_after = timedelta(
        days=10
    )
    user = models.ForeignKey(
        verbose_name=_("user"),
        to=settings.AUTH_USER_MODEL,
        related_name="emails",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    validation_code = models.CharField(
        verbose_name=_("validation code"),
        max_length=200,
        blank=True,
    )
    validated = models.BooleanField(
        verbose_name=_("validated"),
        default=False,
    )
    email = models.EmailField(
        verbose_name=_("email"),
        unique=True,
    )
    main_email = models.BooleanField(
        verbose_name=_("main email"),
        default=False,
    )
    objects = UserEmailManager()

    class Meta:
        verbose_name = _("User E-Mail")
        verbose_name_plural = _("User E-Mails")

    def __str__(self):
        return self.email

    def generate_new_validation_code(self):
        self.validation_code = code_generator()
        self.save()
        return self.validation_code

    def validate(self, user):
        self.validated = True
        self.validation_code = ''
        self.user = user
        self.save()

    @property
    def expired(self):
        if not self.validated:
            now = datetime.now()
            expired_time = self.created.replace(tzinfo=None) + self.expired_after
            if now > expired_time:
                return True
        return False

    @property
    def expired_since(self):
        if not self.validated:
            return self.created.replace(tzinfo=None) + self.expired_after
        return False
