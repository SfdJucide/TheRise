from django.db import models

class Task(models.Model):
    class Statuses(models.IntegerChoices):
        COMPLETED = 1, 'Completed'
        IN_PROGRESS = 2, 'In progress'
        NOT_STARTED = 3, 'Not started'

    class Ranks(models.IntegerChoices):
        BIG = 1, 'Important'
        MID = 2, 'Average'
        SMALL = 3, 'Small'
        __empty__ = 'Выберите насколько важна задача'

    name = models.CharField(max_length=60, verbose_name='Название', db_index=True)
    status = models.IntegerField(choices=Statuses.choices, default=Statuses.NOT_STARTED)
    rank = models.IntegerField(choices=Ranks.choices)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self) -> str:
        return self.name
