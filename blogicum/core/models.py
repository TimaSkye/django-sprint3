from django.db import models


class PublishBaseModel(models.Model):
    """
    Абстрактная модель.
    Поля 'Опубликовано' и 'Дата создания'.
    """

    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено')

    class Meta:
        abstract = True


class TruncleTitleModel(models.Model):
    """Абстрактная модель вывода срезанного title."""

    class Meta:
        abstract = True

    def __str__(self):
        return self.title[:30] + ('...' if len(self.title) > 30 else '')


class TruncleNameModel(models.Model):
    """Абстрактная модель вывода срезанного name."""

    def __str__(self):
        return self.name[:30] + ('...' if len(self.name) > 30 else '')

    class Meta:
        abstract = True
