from django.shortcuts import render, redirect, reverse
from users.mixins import LoginRequiredMixin
from django.views import generic
from .models import Product
from .forms import ProductModelForm

# Create your views here.


class ProductListView(LoginRequiredMixin, generic.ListView):
    template_name = "products/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        active_user = self.request.user
        return Product.objects.filter(user=active_user)


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_queryset(self):
        active_user = self.request.user
        return Product.objects.filter(user=active_user)


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "products/product_create.html"
    form_class = ProductModelForm

    def get_success_url(self):
        return reverse("products:product-list")

    def form_valid(self, form):
        product = form.save(commit=False)
        product.user = self.request.user
        product.save()
        return super(ProductCreateView, self).form_valid(form)


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "products/product_update.html"
    form_class = ProductModelForm

    def get_success_url(self):
        return reverse("products:product-list")

    def get_queryset(self):
        active_user = self.request.user
        return Product.objects.filter(user=active_user)


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "products/product_delete.html"

    def get_success_url(self):
        return reverse("products:product-list")

    def get_queryset(self):
        active_user = self.request.user
        return Product.objects.filter(user=active_user)
