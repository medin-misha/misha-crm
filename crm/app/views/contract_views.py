from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from django.urls import reverse_lazy
from ..models import Service, AdCompany, Client, Contract


class ContractListView(ListView):
    template_name = "contracts/contracts-list.html"
    model = Contract
    context_object_name = "contracts"


class ContractCreateView(CreateView):
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


class ContractDetailView(DetailView):
    template_name = "contracts/contracts-detail.html"
    model = Contract


class ContractUpdateView(UpdateView):
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


class ContractDeleteView(DeleteView):
    template_name = "contracts/contracts-delete.html"
    model = Contract

    def get_success_url(self):
        return reverse_lazy("app:contracts-list")
