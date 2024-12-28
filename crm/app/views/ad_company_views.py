from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from ..models import Service, AdCompany, Client, Contract


class AdCompanyListView(ListView):
    template_name = "ads/ads-list.html"
    model = AdCompany
    context_object_name = "ads"


class AdCompanyCreateView(CreateView):
    template_name = "ads/ads-create.html"
    model = AdCompany
    fields = "name", "service", "promotional_channel", "budget"

    def get_success_url(self):
        return reverse_lazy("app:ads-list")


class AdCompanyUpdateView(UpdateView):
    template_name = "ads/ads-edit.html"
    model = AdCompany
    fields = "name", "service", "promotional_channel", "budget"

    def get_success_url(self):
        return reverse_lazy("app:ads-list")


class AdCompanyDetailView(DetailView):
    template_name = "ads/ads-detail.html"
    model = AdCompany


class AdCompanyDeleteView(DeleteView):
    template_name = "ads/ads-delete.html"
    model = AdCompany

    def get_success_url(self):
        return reverse_lazy("app:ads-list")


class AdCompanyStatisticView(TemplateView):
    template_name = "ads/ads-statistic.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ads"] = AdCompany.objects.all()
        return context