from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('description', 'status', 'due_date')
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Опишите задачу',
            }),
            'status': forms.Select(),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }
