from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .email import Email
from .profile import Profile
from ..managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name=_('username'),
        max_length=254,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(
        verbose_name=_('first name'),
        max_length=30,
        blank=True
    )
    middle_name = models.CharField(
        verbose_name=_('middle name'),
        max_length=30,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name=_('last name'),
        max_length=30,
        blank=True
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(
        verbose_name=_('date joined'),
        default=timezone.now
    )
    is_developer = models.BooleanField(
        verbose_name=_('is developer'),
        default=False,
        blank=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.full_name or self.username

    @property
    def email(self):
        email = Email.objects.get_main_email(self)
        if not email:
            return ''
        return email.email

    def get_email(self):
        return Email.objects.get_main_email(self)

    @property
    def full_name(self):
        return self.get_full_name()

    def get_full_name(self):
        names = list(filter(None, (self.first_name, self.middle_name, self.last_name)))
        return ' '.join(names).strip()

    def get_short_name(self):
        return self.first_name

    def get_profile(self):
        profile = Profile.objects.get(user=self)
        return profile

    def get_validated_emails(self):
        return Email.objects.get_validated_emails(user=self)
