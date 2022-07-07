from django.shortcuts import render

from tasks.models import Task

def tasks_list(request):
    context = {
        'title': 'Список задач',
        'tasks': Task.objects.all()
    }
    return render(request, 'task_list.html', context)
