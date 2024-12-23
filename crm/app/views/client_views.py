from django.views.generic import ListView
from .models import Service, AdCompany, Client, Contract


class ActiveClientListView(ListView):
    template_name = "customers/customers-list.html"
    queryset = Client.objects.filter(is_active=True).all()
    context_object_name = "customers"


class ClientListView(ListView):
    template_name = "leads/leads-list.html"
    queryset = Client.objects.filter(is_active=False).all()
    context_object_name = "leads"
