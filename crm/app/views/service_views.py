from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import Service, AdCompany, Client, Contract


class ServiceListView(LoginRequiredMixin, ListView):
    template_name = "products/products-list.html"
    model = Service
    context_object_name = "products"


class ServiceCreateView(LoginRequiredMixin, CreateView):
    template_name = "products/products-create.html"
    model = Service
    fields = (
        "name",
        "description",
        "price",
    )

    def get_success_url(self):
        return reverse_lazy("app:services-list")


class ServiceDetailView(LoginRequiredMixin, DetailView):
    template_name = "products/products-detail.html"
    model = Service


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "products/products-edit.html"
    model = Service
    fields = (
        "name",
        "description",
        "price",
    )

    def get_success_url(self):
        return reverse_lazy("app:services-detail", kwargs={"pk": self.object.pk})


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "products/products-delete.html"
    model = Service

    def get_success_url(self):
        return reverse_lazy("app:services-list")
