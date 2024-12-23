from django.views.generic import ListView
from .models import Service, AdCompany, Client, Contract


class AdCompanyListView(ListView):
    template_name = "ads/ads-list.html"
    model = AdCompany
    context_object_name = "ads"
