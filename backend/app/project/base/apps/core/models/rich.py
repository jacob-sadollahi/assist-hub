from django.db import models


class RichModel(models.Model):
    class Meta:
        abstract = True

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            if hasattr(self, attr) and value is not None:
                if self._meta.get_field(attr).many_to_many:
                    m2m_objects = getattr(self, attr).all().values_list('id')
                    removal_objects = list(set(m2m_objects) - set(value))
                    additional_objects = list(set(value) - set(m2m_objects))
                    getattr(self, attr).remove(*removal_objects)
                    getattr(self, attr).add(*additional_objects)
                else:
                    setattr(self, attr, value)
        self.save()
