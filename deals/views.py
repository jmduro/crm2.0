from django.shortcuts import render, redirect, reverse
from users.mixins import LoginRequiredMixin
from django.views import generic
from .models import Deal
from .forms import DealModelForm

# Create your views here.


class DealListView(LoginRequiredMixin, generic.ListView):
    template_name = 'deals/deal_list.html'
    context_object_name = 'deals'

    def get_queryset(self):
        active_user = self.request.user
        return Deal.objects.filter(user=active_user)


class DealDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'deals/deal_detail.html'

    def get_queryset(self):
        active_user = self.request.user
        return Deal.objects.filter(user=active_user)


class DealCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "deals/deal_create.html"
    context_object_name = 'deals'
    form_class = DealModelForm

    def form_valid(self, form):
        deal = form.save(commit=False)
        deal.user = self.request.user
        deal.save()
        return super(DealCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("deals:deal-list")


class DealUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "deals/deal_update.html"
    form_class = DealModelForm

    def get_queryset(self):
        active_user = self.request.user
        return Deal.objects.filter(user=active_user)

    def get_success_url(self):
        return reverse("deals:deal-list")


class DealDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "deals/deal_delete.html"

    def get_success_url(self):
        return reverse("deals:deal-list")

    def get_queryset(self):
        active_user = self.request.user
        return Deal.objects.filter(user=active_user)
