from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskViewTests(TestCase):
    def test_task_list_displays_tasks(self):
        Task.objects.create(
            description='Проверить список задач',
            detailed_description='Это подробное описание не должно быть на главной',
            status=Task.NEW,
            due_date=date(2026, 5, 27),
        )

        response = self.client.get(reverse('task_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Проверить список задач')
        self.assertContains(response, '2026-05-27')
        self.assertNotContains(response, 'Это подробное описание не должно быть на главной')

    def test_task_can_be_created(self):
        response = self.client.post(reverse('task_list'), {
            'description': 'Добавить задачу через форму',
            'detailed_description': 'Подробности новой задачи',
            'status': Task.IN_PROGRESS,
            'due_date': '2026-05-28',
        })

        self.assertRedirects(response, reverse('task_list'))
        self.assertTrue(Task.objects.filter(
            description='Добавить задачу через форму',
            status=Task.IN_PROGRESS,
            detailed_description='Подробности новой задачи',
        ).exists())

    def test_task_detail_displays_all_fields(self):
        task = Task.objects.create(
            description='Открыть детали задачи',
            detailed_description='Первая строка\n  Вторая строка с отступом',
            status=Task.IN_PROGRESS,
            due_date=date(2026, 5, 30),
        )

        response = self.client.get(reverse('task_detail', args=[task.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Открыть детали задачи')
        self.assertContains(response, 'В процессе')
        self.assertContains(response, '2026-05-30')
        self.assertContains(response, 'Первая строка<br>')
        self.assertContains(response, '  Вторая строка с отступом')

    def test_task_can_be_deleted(self):
        task = Task.objects.create(
            description='Удалить без подтверждения',
            status=Task.DONE,
            due_date=date(2026, 5, 29),
        )

        response = self.client.post(reverse('task_delete', args=[task.pk]))

        self.assertRedirects(response, reverse('task_list'))
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())
