from django.utils import translation
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from project.base.apps.translation.models import Translation
from .serializers import TranslationSerializer
from ..caching import CustomListKeyConstructor


class ListTranslations(GenericAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()
    list_cache_key_func = CustomListKeyConstructor()

    def get(self, request, *args, **kwargs):
        cur_language = translation.get_language()
        translation.activate(kwargs.get('lang', 'en'))
        translations = {t.key: t.value for t in Translation.objects.all()}
        translation.activate(cur_language)
        return Response(translations, 200)
