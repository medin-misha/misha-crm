from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Service, AdCompany, Client


# Create your views here.

class UsersIndexView(TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products_count"] = Service.objects.all().distinct().count()
        context["advertisements_count"] = AdCompany.objects.all().distinct().count()
        context["leads_count"] = Client.objects.filter(is_active=False).all().distinct().count()
        context["customers_count"] = Client.objects.filter(is_active=True).all().distinct().count()

        return context
