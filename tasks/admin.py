from django.contrib import admin
from . import models


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'description', 'deadline', 'priority')


admin.site.register(models.Task, TaskAdmin)
