from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from project.base.apps.email.models import Email, MailBindr


class EmailDetailsView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        email = get_object_or_404(Email, pk=pk)
        return HttpResponse(email.compiled_template)


class MailBindrHtmlView(View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, pk):
        email = get_object_or_404(MailBindr, pk=pk)
        return HttpResponse(email.html_body)
