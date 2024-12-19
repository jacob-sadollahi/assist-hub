from django.contrib import admin
from django.db import models
from django.forms import Textarea

from .models import Translation
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(Translation)
class TranslationAdmin(TabbedTranslationAdmin):
    search_fields = ['key', 'value', 'value_de', 'value_en']
    list_display = ['created', 'key', 'value_en', 'value_de']
    list_editable = ['key', 'value_en', 'value_de']
    list_filter = ['created']
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
            attrs={
                'rows': 1,
                'cols': 40,
                'style': 'height: 1em;',
            }
        )},
    }
