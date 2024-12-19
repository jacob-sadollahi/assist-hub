from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from project.apps.rest.core.permissions import IsDeveloperPermission
from project.apps.rest.core.schema import BothHttpAndHttpsSchemaGenerator
from project.settings import WEBSITE_URL

app_name = 'rest_api'

schema_view = get_schema_view(
    openapi.Info(
        title="AssistHub API",
        default_version='v1',
        description="AssistHub API Application",
        terms_of_service=f"{WEBSITE_URL}/terms/",
        contact=openapi.Contact(email="jacob.sadollahi@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=[IsDeveloperPermission],
)

urlpatterns = [
    path('auth/', include('project.apps.rest.auth.urls')),
    path('translations/', include('project.apps.rest.translation.urls')),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]
