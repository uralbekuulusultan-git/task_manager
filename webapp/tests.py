from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskViewTests(TestCase):
    def test_task_list_displays_tasks(self):
        Task.objects.create(
            description='Проверить список задач',
            status=Task.NEW,
            due_date=date(2026, 5, 27),
        )

        response = self.client.get(reverse('task_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Проверить список задач')
        self.assertContains(response, '2026-05-27')

    def test_task_can_be_created(self):
        response = self.client.post(reverse('task_list'), {
            'description': 'Добавить задачу через форму',
            'status': Task.IN_PROGRESS,
            'due_date': '2026-05-28',
        })

        self.assertRedirects(response, reverse('task_list'))
        self.assertTrue(Task.objects.filter(
            description='Добавить задачу через форму',
            status=Task.IN_PROGRESS,
        ).exists())

    def test_task_can_be_deleted(self):
        task = Task.objects.create(
            description='Удалить без подтверждения',
            status=Task.DONE,
            due_date=date(2026, 5, 29),
        )

        response = self.client.post(reverse('task_delete', args=[task.pk]))

        self.assertRedirects(response, reverse('task_list'))
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())
