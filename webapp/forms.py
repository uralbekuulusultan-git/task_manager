from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('description', 'detailed_description', 'status', 'due_date')
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Опишите задачу',
            }),
            'detailed_description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Добавьте подробности, шаги или заметки',
            }),
            'status': forms.Select(),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
