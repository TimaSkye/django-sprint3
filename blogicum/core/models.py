from django.db import models


class PublishBaseModel(models.Model):
    """
    Абстрактная модель.
    Поля 'Опубликовано' и 'Дата создания'.
    """
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
