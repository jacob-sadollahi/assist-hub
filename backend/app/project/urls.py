"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.views.i18n import set_language

from project import settings
from project.base.apps.core.views import health_check


def trigger_error(request):  # noqa
    division_by_zero = 1 / 0  # noqa


admin.site.site_url = settings.FRONTEND_URL
admin.site.site_header = _("Assist-hub Admin")
admin.site.site_title = _("Assist-hub Admin")
admin.site.index_title = _("Welcome to the assist-hub the Admin Interface!")

urlpatterns = [
    path('i18n/', set_language, name='set_language'),
    path("api/", include("project.apps.rest.urls", namespace="api")),
    path("email/", include("project.base.apps.email.urls", namespace="email")),
    path('health-check/', health_check),
    path('sentry-debug/', trigger_error),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
)

if settings.DEBUG:
    import warnings

    try:
        import debug_toolbar
    except ImportError:
        warnings.warn(
            "The debug toolbar was not installed. Ignore the error. \
            settings.py should already have warned the user about it."
        )
    else:
        urlpatterns += [path("backend/__debug__/", include(debug_toolbar.urls))]

    if settings.ENABLE_DEBUG_SILK:
        try:
            import silk  # noqa
        except ImportError:
            warnings.warn(
                "The debug silk was not installed. Ignore the error. \
                settings.py should already have warned the user about it."
            )
        else:
            urlpatterns += [path('silk/', include("silk.urls", namespace='silk'))]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
