from django.db import models
from tasks.models import Task


class Weekday(models.Model):
    big_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    percents = models.PositiveIntegerField(verbose_name='проценты')


class Weekend(Weekday):
    pass
