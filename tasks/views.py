from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models


class TaskListView(ListView):
    model = models.Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = models.Task
    template_name = 'task_create.html'
    fields = ['title']
    success_url = reverse_lazy('task:list')


class TaskDetailView(DetailView):
    model = models.Task
    template_name = 'task_detail.html'


class TaskUpdateView(UpdateView):
    model = models.Task
    template_name = 'task_update.html'
    fields = ['title']
    success_url = reverse_lazy('task:list')


class TaskDeleteView(DeleteView):
    model = models.Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task:list')
