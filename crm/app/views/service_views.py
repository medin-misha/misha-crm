from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from ..models import Service, AdCompany, Client, Contract


class ServiceListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "app.view_service"
    template_name = "products/products-list.html"
    model = Service
    context_object_name = "products"


class ServiceCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "app.add_service"
    template_name = "products/products-create.html"
    model = Service
    fields = (
        "name",
        "description",
        "price",
    )

    def get_success_url(self):
        return reverse_lazy("app:services-list")


class ServiceDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = "app.view_service"
    template_name = "products/products-detail.html"
    model = Service


class ServiceUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "app.change_service"
    template_name = "products/products-edit.html"
    model = Service
    fields = (
        "name",
        "description",
        "price",
    )

    def get_success_url(self):
        return reverse_lazy("app:services-detail", kwargs={"pk": self.object.pk})


class ServiceDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = "app.delete_service"
    template_name = "products/products-delete.html"
    model = Service

    def get_success_url(self):
        return reverse_lazy("app:services-list")
