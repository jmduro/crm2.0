from django.shortcuts import render, redirect, reverse
from users.mixins import LoginRequiredMixin, StaffAndLoginRequiredMixin
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


class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = 'deals/category_list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        active_user = self.request.user
        queryset = Deal.objects.filter(user=active_user)

        uncategorized_deal_count = queryset.filter(
            stage=Deal.UNCATEGORIZED).count()
        classification_deal_count = queryset.filter(
            stage=Deal.CLASSIFICATION).count()
        sizing_deal_count = queryset.filter(stage=Deal.SIZING).count()
        quotation_deal_count = queryset.filter(
            stage=Deal.QUOTATION).count()
        negotiation_deal_count = queryset.filter(
            stage=Deal.NEGOTIATION).count()
        invoiced_deal_count = queryset.filter(
            stage=Deal.INVOICED).count()
        paid_out_deal_count = queryset.filter(
            stage=Deal.PAID_OUT).count()
        closed_won_deal_count = queryset.filter(
            stage=Deal.CLOSED_WON).count()
        closed_lost_deal_count = queryset.filter(
            stage=Deal.CLOSED_LOST).count()

        category_list = [
            Category('Uncategorized', uncategorized_deal_count),
            Category('Classification', classification_deal_count),
            Category('Sizing', sizing_deal_count),
            Category('Quotation', quotation_deal_count),
            Category('Negotiation', negotiation_deal_count),
            Category('Invoiced', invoiced_deal_count),
            Category('Paid Out', paid_out_deal_count),
            Category('Closed Won', closed_won_deal_count),
            Category('Closed Lost', closed_lost_deal_count),
        ]

        context.update({
            'category_list': category_list,
        })

        return context

    def get_queryset(self):
        active_user = self.request.user
        return Deal.objects.filter(user=active_user)


class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'deals/category_detail.html'
    context_object_name = 'name'

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        active_user = self.request.user
        queryset = Deal.objects.filter(user=active_user)

        uncategorized_deals = queryset.filter(stage=Deal.UNCATEGORIZED)
        classification_deals = queryset.filter(stage=Deal.CLASSIFICATION)
        sizing_deals = queryset.filter(stage=Deal.SIZING)
        quotation_deals = queryset.filter(stage=Deal.QUOTATION)
        negotiation_deals = queryset.filter(stage=Deal.NEGOTIATION)
        invoiced_deals = queryset.filter(stage=Deal.INVOICED)
        paid_out_deals = queryset.filter(stage=Deal.PAID_OUT)
        closed_won_deals = queryset.filter(stage=Deal.CLOSED_WON)
        closed_lost_deals = queryset.filter(stage=Deal.CLOSED_LOST)

        category_list = [
            ('Uncategorized', uncategorized_deals),
            ('Classification', classification_deals),
            ('Sizing', sizing_deals),
            ('Quotation', quotation_deals),
            ('Negotiation', negotiation_deals),
            ('Invoiced', invoiced_deals),
            ('Paid Out', paid_out_deals),
            ('Closed Won', closed_won_deals),
            ('Closed Lost', closed_lost_deals),
        ]

        context.update({
            'category_list': category_list,
        })
        return context

    def get_queryset(self):
        active_user = self.request.user
        return Deal.objects.filter(user=active_user)


class Category():

    def __init__(self, name: str, count: int):
        self.name = name
        self.count = count
