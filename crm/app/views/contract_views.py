from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from ..models import Service, AdCompany, Client, Contract


class ContractListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "app.view_contract"
    template_name = "contracts/contracts-list.html"
    model = Contract
    context_object_name = "contracts"


class ContractCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "app.add_contract"
    template_name = "contracts/contracts-create.html"
    model = Contract
    fields = (
        "name",
        "service",
        "client",
        "document",
        "conclusion_date",
        "days_of_action",
        "price",
    )

    def get_success_url(self):
        return reverse_lazy("app:contracts-list")


class ContractDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = "app.view_contract"
    template_name = "contracts/contracts-detail.html"
    model = Contract


class ContractUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "app.change_contract"
    template_name = "contracts/contracts-edit.html"
    model = Contract
    fields = (
        "name",
        "service",
        "client",
        "document",
        "conclusion_date",
        "days_of_action",
        "price",
    )

    def get_success_url(self):
        return reverse_lazy("app:contracts-list")


class ContractDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = "app.delete_contract"
    template_name = "contracts/contracts-delete.html"
    model = Contract

    def get_success_url(self):
        return reverse_lazy("app:contracts-list")
