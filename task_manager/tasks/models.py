from django.db import models


class TaskStatus(models.TextChoices):
    NEW = 'NEW', 'Новая задача'
    IN_PROGRESS = 'IN_PROGRESS', 'В процессе работы'
    COMPLETED = 'COMPLETED', 'Завершено успешно'
    ERROR = 'ERROR', 'Ошибка'


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.NEW
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
