from dataclasses import dataclass

from .forms import TaskForm
from .models import Task


@dataclass(frozen=True)
class TaskListViewModel:
    tasks: object
    form: TaskForm
    total_count: int
    new_count: int
    in_progress_count: int
    done_count: int

    @classmethod
    def build(cls, form=None):
        tasks = Task.objects.all()

        return cls(
            tasks=tasks,
            form=form or TaskForm(),
            total_count=tasks.count(),
            new_count=tasks.filter(status=Task.NEW).count(),
            in_progress_count=tasks.filter(status=Task.IN_PROGRESS).count(),
            done_count=tasks.filter(status=Task.DONE).count(),
        )
