from django.shortcuts import render, redirect, reverse
from users.mixins import LoginRequiredMixin
from django.views import generic
from .models import Task
from .forms import TaskModelForm

# Create your views here.


class TaskListView(LoginRequiredMixin, generic.ListView):
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        active_user = self.request.user
        return Task.objects.filter(user=active_user)


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        active_user = self.request.user
        return Task.objects.filter(user=active_user)


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'tasks/task_create.html'
    form_class = TaskModelForm

    def get_form_kwargs(self):
        return {'request': self.request}

    def get_success_url(self):
        return reverse('tasks:task-list')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.save()
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'tasks/task_update.html'
    form_class = TaskModelForm

    def get_form_kwargs(self):
        return {'request': self.request}

    def get_success_url(self):
        return reverse('tasks:task-list')

    def get_queryset(self):
        active_user = self.request.user
        return Task.objects.filter(user=active_user)


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'tasks/task_delete.html'

    def get_success_url(self):
        return reverse('tasks:task-list')

    def get_queryset(self):
        active_user = self.request.user
        return Task.objects.filter(user=active_user)
