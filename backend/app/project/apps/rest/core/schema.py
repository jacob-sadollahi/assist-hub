from drf_yasg.generators import OpenAPISchemaGenerator

from project.settings import DEBUG


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http" if DEBUG else "https"]
        return schema
