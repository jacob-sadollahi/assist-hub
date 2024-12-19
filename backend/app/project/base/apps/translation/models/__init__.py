import datetime

from django.core.cache import cache
from django.db.models.signals import post_save, post_delete

from .translation import Translation  # noqa


def updated_at(sender=None, instance=None, *args, **kwargs):
    # This is used to invalidate the cache for the apis
    cache.set('api_updated_at_timestamp', datetime.datetime.utcnow())


for model in [Translation]:
    post_save.connect(receiver=updated_at, sender=model)
    post_delete.connect(receiver=updated_at, sender=model)
