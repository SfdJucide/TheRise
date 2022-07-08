from django.contrib import admin

from tasks.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'status')
    list_display_links = ('name',)
    search_fields = ('name',)
