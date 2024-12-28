from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import Service, AdCompany, Client, Contract


class UsersIndexView(LoginRequiredMixin, TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["service_count"] = Service.objects.all().distinct().count()
        context["advertisements_count"] = AdCompany.objects.all().distinct().count()
        context["clients_count"] = (
            Client.objects.filter(is_active=False).all().distinct().count()
        )
        context["active_clients_count"] = (
            Client.objects.filter(is_active=True).all().distinct().count()
        )

        return context


class UserLoginView(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):
        return reverse_lazy("app:user-index")


class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

