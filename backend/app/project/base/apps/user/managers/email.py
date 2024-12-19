from django.db import models


class UserEmailManager(models.Manager):
    @staticmethod
    def _lower_email(kwargs):
        if 'email' in kwargs:
            kwargs['email'] = kwargs['email'].lower()
        return kwargs

    def filter(self, **kwargs):
        kwargs = self._lower_email(kwargs)
        return super(UserEmailManager, self).filter(**kwargs)

    def get(self, **kwargs):
        kwargs = self._lower_email(kwargs)
        return super(UserEmailManager, self).get(**kwargs)

    def create(self, **kwargs):
        kwargs = self._lower_email(kwargs)
        return super(UserEmailManager, self).create(**kwargs)

    def get_main_email(self, user):
        try:
            main_email = self.model.objects.get(user=user, main_email=True)
        except self.model.DoesNotExist:
            emails = self.model.objects.filter(user=user)
            if emails:
                main_email = emails.order_by("-created")[0]
                main_email.main_email = True
                main_email.save()
            else:
                return None
        return main_email

    def get_validated_emails(self, user):
        return self.model.objects.filter(user=user, validated=True)
