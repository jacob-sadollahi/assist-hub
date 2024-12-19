from django.urls import path

from .views import ListTranslations

urlpatterns = [
    path('<str:lang>/', ListTranslations.as_view(), name="list-translations"),
]
