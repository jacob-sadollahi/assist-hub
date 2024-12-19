from django.db import models


class SortableModel(models.Model):
    sort_order = models.PositiveIntegerField(
        default=0,
        db_index=True,
        blank=False,
        null=False,
    )

    class Meta:
        abstract = True
