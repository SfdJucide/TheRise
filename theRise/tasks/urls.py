from django.urls import path

from tasks.views import tasks_list

app_name = 'tasks'

urlpatterns = [
    path('', tasks_list, name='tasks_list'),
]