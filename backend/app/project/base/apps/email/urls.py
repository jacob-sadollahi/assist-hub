from django.urls import path

from . import views

app_name = 'email'
urlpatterns = [
    path('<int:pk>/', views.EmailDetailsView.as_view(), name='emails-detail-view'),
    path('mailbindr/<uuid:pk>/', views.MailBindrHtmlView.as_view(), name='mailbindr-html-view'),
]
