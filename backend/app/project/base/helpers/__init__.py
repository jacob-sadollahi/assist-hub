import os
import random
from io import StringIO

from django.core.handlers.wsgi import WSGIRequest

from project import settings


def django_request():
    schema = 'http'
    host = 'localhost:8877'
    if not settings.DEBUG:
        host = os.environ.get('DOMAIN')
        schema = 'https'
    meta = {
        'wsgi.url_scheme': schema,
        'HTTP_HOST': host,
        'REQUEST_METHOD': 'GET',
        'PATH_INFO': '/',
        'wsgi.input': StringIO(),
    }
    return WSGIRequest(meta)


def code_generator(length=5):
    numbers = '0123456789'
    return ''.join(random.choice(numbers) for i in range(length))


def get_base_url() -> str:
    if settings.DEBUG:
        return 'http://localhost:8892'
    return f'https://{settings.BACKEND_DOMAIN}'
