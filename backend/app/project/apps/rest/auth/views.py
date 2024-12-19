from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView

from project.settings import SIMPLE_JWT


class LogoutAPIView(APIView):
    redirect = None  # provide redirect url if required

    def get(self, request, *args, **kwargs):
        logout(request)
        if self.redirect:
            response = HttpResponseRedirect(self.redirect)
        else:
            response = Response('OK')
        response.delete_cookie(
            key=SIMPLE_JWT.get('COOKIE'),
            domain=settings.SESSION_COOKIE_DOMAIN,
        )
        return response
