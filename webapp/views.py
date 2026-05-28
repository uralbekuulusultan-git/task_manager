from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task
from .viewmodels import TaskListViewModel


def task_list(request):
    form = TaskForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('task_list')

    view_model = TaskListViewModel.build(form=form)
    return render(request, 'webapp/task_list.html', {'view_model': view_model})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'webapp/task_detail.html', {'task': task})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()

    return redirect('task_list')
