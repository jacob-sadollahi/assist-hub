import datetime

from django.core.cache import cache
from django.utils.encoding import force_str
from rest_framework_extensions.key_constructor.bits import KeyBitBase, RetrieveSqlQueryKeyBit, PaginationKeyBit, \
    ListSqlQueryKeyBit
from rest_framework_extensions.key_constructor.constructors import DefaultKeyConstructor


class UpdatedAtKeyBit(KeyBitBase):
    def get_data(self, **kwargs):
        key = 'api_updated_at_timestamp'
        value = cache.get(key, None)
        if not value:
            value = datetime.datetime.utcnow()
            cache.set(key, value=value)
        return force_str(value)


class CustomObjectKeyConstructor(DefaultKeyConstructor):
    retrieve_sql = RetrieveSqlQueryKeyBit()
    updated_at = UpdatedAtKeyBit()


class LatestObjectKeyConstructor(DefaultKeyConstructor):
    retrieve_sql = ListSqlQueryKeyBit()
    updated_at = UpdatedAtKeyBit()


class CustomListKeyConstructor(DefaultKeyConstructor):
    list_sql = ListSqlQueryKeyBit()
    pagination = PaginationKeyBit()
    updated_at = UpdatedAtKeyBit()
