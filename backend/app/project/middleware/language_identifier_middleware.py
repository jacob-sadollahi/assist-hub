from project.settings import LANGUAGES, MODELTRANSLATION_DEFAULT_LANGUAGE


class LanguageIdentificationMiddleware(object):
    """ Middleware for adding Accept-Language into a custom attr in request"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.LANG = request.headers.get('Accept-Language')
        if request.LANG and (
                request.LANG.lower() not in dict(LANGUAGES).keys() or
                request.LANG.lower() in MODELTRANSLATION_DEFAULT_LANGUAGE):
            request.LANG = None
        return self.get_response(request)
