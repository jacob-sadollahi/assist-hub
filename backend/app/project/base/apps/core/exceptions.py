from project.settings import _


class BaseHttpError(Exception):
    default_msg = 'The connection error'

    def __init__(self, message=None, *args, **kwargs):
        super(BaseHttpError, self).__init__(*args, **kwargs)
        self.message = message

    def __str__(self):
        return self.message or self.default_msg


class HttpBadRequestError(BaseHttpError):
    default_msg = _('Bad request error.')


class HttpServerError(BaseHttpError):
    default_msg = _('We have internal server errors')
