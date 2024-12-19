from modeltranslation.translator import register, TranslationOptions
from .models import Translation


@register(Translation)
class TranslationOptions(TranslationOptions):
    fields = [
        'value',
    ]
