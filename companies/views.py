from django.shortcuts import render, redirect, reverse
from users.mixins import LoginRequiredMixin
from django.views import generic
from .models import Company
from .forms import CompanyModelForm

# Create your views here.


class CompanyListView(LoginRequiredMixin, generic.ListView):
    template_name = 'companies/company_list.html'
    context_object_name = 'companies'

    def get_queryset(self):
        active_user = self.request.user
        return Company.objects.filter(user=active_user, featured=False)

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        queryset = Company.objects.filter(featured=True)
        context.update({
            'featured_companies': queryset
        })
        return context


class CompanyDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'companies/company_detail.html'
    context_object_name = 'company'

    def get_queryset(self):
        active_user = self.request.user
        return Company.objects.filter(user=active_user)


class CompanyCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'companies/company_create.html'
    form_class = CompanyModelForm

    def get_success_url(self):
        return reverse('companies:company-list')

    def form_valid(self, form):
        company = form.save(commit=False)
        company.user = self.request.user
        company.save()
        return super(CompanyCreateView, self).form_valid(form)


class CompanyUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'companies/company_update.html'
    form_class = CompanyModelForm

    def get_success_url(self):
        return reverse('companies:company-list')

    def get_queryset(self):
        active_user = self.request.user
        return Company.objects.filter(user=active_user)


class CompanyDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'companies/company_delete.html'

    def get_success_url(self):
        return reverse('companies:company-list')

    def get_queryset(self):
        active_user = self.request.user
        return Company.objects.filter(user=active_user)
