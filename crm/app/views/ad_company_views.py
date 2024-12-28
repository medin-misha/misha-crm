from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from ..models import Service, AdCompany, Client, Contract


class AdCompanyListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "app.view_adcompany"
    template_name = "ads/ads-list.html"
    model = AdCompany
    context_object_name = "ads"


class AdCompanyCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "app.add_adcompany"
    template_name = "ads/ads-create.html"
    model = AdCompany
    fields = "name", "service", "promotional_channel", "budget"

    def get_success_url(self):
        return reverse_lazy("app:ads-list")


class AdCompanyUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "app.change_adcompany"
    template_name = "ads/ads-edit.html"
    model = AdCompany
    fields = "name", "service", "promotional_channel", "budget"

    def get_success_url(self):
        return reverse_lazy("app:ads-list")


class AdCompanyDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = "app.view_adcompany"
    template_name = "ads/ads-detail.html"
    model = AdCompany


class AdCompanyDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = "app.delete_adcompany"
    template_name = "ads/ads-delete.html"
    model = AdCompany

    def get_success_url(self):
        return reverse_lazy("app:ads-list")


class AdCompanyStatisticView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    permission_required = "app.view_adcompany"
    template_name = "ads/ads-statistic.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ads"] = AdCompany.objects.all()
        return context