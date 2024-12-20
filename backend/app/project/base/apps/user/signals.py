from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from project.base.apps.user.models import Profile

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    Profile.objects.get_or_create(user=instance)
