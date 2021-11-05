from django.shortcuts import reverse, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from users.mixins import LoginRequiredMixin
from .models import Contact
from .forms import ContactModelForm
# Create your views here.


class ContactListView(LoginRequiredMixin, generic.ListView):
    template_name = 'contacts/contact_list.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        active_user = self.request.user
        return Contact.objects.filter(user=active_user)

    def get_context_data(self, **kwargs):
        context = super(ContactListView, self).get_context_data(**kwargs)
        queryset = Contact.objects.filter(featured=True)
        context.update({
            'featured_contacts': queryset
        })
        return context


class ContactDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'contacts/contact_detail.html'

    def get_queryset(self):
        active_user = self.request.user
        return Contact.objects.filter(user=active_user)


class ContactCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'contacts/contact_create.html'
    context_object_name = 'contacts'
    form_class = ContactModelForm

    def form_valid(self, form):
        company = form.save(commit=False)
        company.user = self.request.user
        company.save()
        return super(ContactCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('contacts:contact-list')


class ContactUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'contacts/contact_update.html'
    form_class = ContactModelForm

    def get_queryset(self):
        active_user = self.request.user
        return Contact.objects.filter(user=active_user)

    def get_success_url(self):
        return reverse('contacts:contact-list')


class ContactDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'contacts/contact_delete.html'

    def get_success_url(self):
        return reverse('contacts:contact-list')

    def get_queryset(self):
        active_user = self.request.user
        return Contact.objects.filter(user=active_user)
