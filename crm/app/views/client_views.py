from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from ..models import Service, AdCompany, Client, Contract


class ActiveClientListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "app.view_client"
    template_name = "leads/leads-list.html"
    queryset = Client.objects.filter(is_active=True).all()
    context_object_name = "leads"


class ClientListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "app.view_client"
    template_name = "leads/leads-list.html"
    queryset = Client.objects.filter(is_active=False).all()
    context_object_name = "leads"


class ClientCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = "app.add_client"
    template_name = "leads/leads-create.html"
    fields = "full_name", "phone", "email", "is_active", "ad_company"
    model = Client

    def get_success_url(self):
        if self.request.POST.get("is_active") is None:
            return reverse_lazy("app:clients-list")
        return reverse_lazy("app:active-client-list")


class ClientDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = "app.view_client"
    template_name = "leads/leads-detail.html"
    model = Client


class ClientUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "app.change_client"
    template_name = "leads/leads-edit.html"
    fields = "full_name", "phone", "email", "is_active", "ad_company"
    model = Client

    def get_success_url(self):
        return reverse_lazy("app:clients-list")


class ClientDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "app.delete_client"
    template_name = "leads/leads-delete.html"
    model = Client

    def get_success_url(self):
        if self.object.is_active is None:
            return reverse_lazy("app:clients-list")
        return reverse_lazy("app:active-client-list")
