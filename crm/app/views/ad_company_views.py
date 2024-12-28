from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Service, AdCompany, Client, Contract


class AdCompanyListView(LoginRequiredMixin, ListView):
    template_name = "ads/ads-list.html"
    model = AdCompany
    context_object_name = "ads"


class AdCompanyCreateView(LoginRequiredMixin, CreateView):
    template_name = "ads/ads-create.html"
    model = AdCompany
    fields = "name", "service", "promotional_channel", "budget"

    def get_success_url(self):
        return reverse_lazy("app:ads-list")


class AdCompanyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "ads/ads-edit.html"
    model = AdCompany
    fields = "name", "service", "promotional_channel", "budget"

    def get_success_url(self):
        return reverse_lazy("app:ads-list")


class AdCompanyDetailView(LoginRequiredMixin, DetailView):
    template_name = "ads/ads-detail.html"
    model = AdCompany


class AdCompanyDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "ads/ads-delete.html"
    model = AdCompany

    def get_success_url(self):
        return reverse_lazy("app:ads-list")


class AdCompanyStatisticView(LoginRequiredMixin, TemplateView):
    template_name = "ads/ads-statistic.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ads"] = AdCompany.objects.all()
        return context