from rest_framework import serializers

from project.base.apps.translation.models import Translation


class TranslationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Translation
        fields = ['key', 'value']
