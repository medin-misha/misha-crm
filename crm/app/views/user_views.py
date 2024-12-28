from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Service, AdCompany, Client, Contract


class UsersIndexView(LoginRequiredMixin, TemplateView):
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products_count"] = Service.objects.all().distinct().count()
        context["advertisements_count"] = AdCompany.objects.all().distinct().count()
        context["leads_count"] = (
            Client.objects.filter(is_active=False).all().distinct().count()
        )
        context["customers_count"] = (
            Client.objects.filter(is_active=True).all().distinct().count()
        )

        return context


class UserLoginView(LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = "app:user-index"


class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == "GET":
            return self.post(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

