from django.views.generic import ListView
from .models import Service, AdCompany, Client, Contract


class ServiceListView(ListView):
    template_name = "products/products-list.html"
    model = Service
    context_object_name = "products"
