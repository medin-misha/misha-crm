from django.views.generic import ListView
from .models import Service, AdCompany, Client, Contract


class ContractListView(ListView):
    template_name = "contracts/contracts-list.html"
    model = Contract
    context_object_name = "contracts"
