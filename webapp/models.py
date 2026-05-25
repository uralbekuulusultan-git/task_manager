from django.db import models


class Task(models.Model):
    NEW = 'new'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'

    STATUS_CHOICES = [
        (NEW, 'Новая'),
        (IN_PROGRESS, 'В процессе'),
        (DONE, 'Сделанно'),
    ]

    description = models.TextField('Описание')
    status = models.CharField(
        'Статус',
        max_length=20,
        choices=STATUS_CHOICES,
        default=NEW,
    )
    due_date = models.DateField('Дата выполнения')

    class Meta:
        ordering = ['due_date', 'id']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.description[:50]
