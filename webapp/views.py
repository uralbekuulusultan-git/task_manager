from django.http import HttpResponse


def task_list(request):
    return HttpResponse('Task manager')
