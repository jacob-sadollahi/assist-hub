from django.db import models
from django.utils.crypto import get_random_string


class BaseUserManager(models.Manager):

    @staticmethod
    def make_random_password(length=10,
                             allowed_chars='abcdefghjkmnpqrstuvwxyz'
                                           'ABCDEFGHJKLMNPQRSTUVWXYZ'
                                           '23456789'):
        return get_random_string(length, allowed_chars)

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})


class UserManager(BaseUserManager):
    use_in_migrations = True

    @staticmethod
    def _lower_username(kwargs):
        if 'username' in kwargs:
            kwargs['username'] = kwargs['username'].lower()
        return kwargs

    def filter(self, **kwargs):
        kwargs = self._lower_username(kwargs)
        return super(UserManager, self).filter(**kwargs)

    def get(self, **kwargs):
        kwargs = self._lower_username(kwargs)
        return super(UserManager, self).get(**kwargs)

    def create(self, **kwargs):
        kwargs = self._lower_username(kwargs)
        return super(UserManager, self).create(**kwargs)

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username.lower(), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)
