from django.shortcuts import render, redirect, reverse
from users.mixins import LoginRequiredMixin
from django.views import generic
from .models import Event
from .forms import EventModelForm

# Create your views here.


class EventListView(LoginRequiredMixin, generic.ListView):
    template_name = "events/events_list.html"
    context_object_name = "events"

    def get_queryset(self):
        active_user = self.request.user
        return Event.objects.filter(user=active_user)


class EventDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "events/event_detail.html"
    context_object_name = "event"

    def get_queryset(self):
        active_user = self.request.user
        return Event.objects.filter(user=active_user)


class EventCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "events/event_create.html"
    form_class = EventModelForm

    def get_success_url(self):
        return reverse("events:event-list")

    def form_valid(self, form):
        event = form.save(commit=False)
        event.user = self.request.user
        event.save()
        return super(EventCreateView, self).form_valid(form)


class EventUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "events/event_update.html"
    form_class = EventModelForm

    def get_success_url(self):
        return reverse("events:event-list")

    def get_queryset(self):
        active_user = self.request.user
        return Event.objects.filter(user=active_user)


class EventDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "events/event_delete.html"

    def get_success_url(self):
        return reverse("events:event-list")

    def get_queryset(self):
        active_user = self.request.user
        return Event.objects.filter(user=active_user)
