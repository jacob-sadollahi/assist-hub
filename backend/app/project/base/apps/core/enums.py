from project.settings import _


class StatusEnum:
    PUBLISH = 'publish'
    DRAFT = 'draft'

    CHOICES = (
        (PUBLISH, _(PUBLISH)),
        (DRAFT, _(DRAFT)),
    )
