from django.shortcuts import render

from tasks.models import Task
from tasks.forms import TaskForm

def tasks_list(request):
    context = {
        'title': 'Список задач',
        'tasks': Task.objects.all(),
        'form': TaskForm
    }
    return render(request, 'task_list.html', context)
