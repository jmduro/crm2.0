from django.shortcuts import render, redirect, reverse
from users.mixins import StaffAndLoginRequiredMixin
from django.views import generic
from .models import User
from .forms import CustomUserCreationForm

# Create your views here.


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class SecondPageView(generic.TemplateView):
    template_name = "second_page.html"


class UserListView(StaffAndLoginRequiredMixin, generic.ListView):
    template_name = "users/user_list.html"
    context_object_name = "users"

    def get_queryset(self):
        return User.objects.all()


class UserDetailView(StaffAndLoginRequiredMixin, generic.DetailView):
    template_name = "users/user_detail.html"
    context_object_name = "user"

    def get_queryset(self):
        return User.objects.all()


class UserCreateView(StaffAndLoginRequiredMixin, generic.CreateView):
    template_name = "users/user_create.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("users:user-list")


class UserUpdateView(StaffAndLoginRequiredMixin, generic.UpdateView):
    template_name = "users/user_update.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("users:user-list")

    def get_queryset(self):
        return User.objects.all()


class UserDeleteView(StaffAndLoginRequiredMixin, generic.DeleteView):
    template_name = "users/user_delete.html"

    def get_success_url(self):
        return reverse("users:user-list")

    def get_queryset(self):
        return User.objects.all()
