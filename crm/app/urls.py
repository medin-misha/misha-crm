from django.urls import path
from .views import (
    user_views,
    ad_company_views,
    client_views,
    contract_views,
    service_views,
)

app_name = "app"

urlpatterns = [
    path("", user_views.UsersIndexView.as_view(), name="user-index"),
    path("services/", service_views.ServiceListView.as_view(), name="services-list"),
    path(
        "services/new/",
        service_views.ServiceCreateView.as_view(),
        name="services-create",
    ),
    path(
        "services/<int:pk>/",
        service_views.ServiceDetailView.as_view(),
        name="services-detail",
    ),
    path(
        "services/delete/<int:pk>",
        service_views.ServiceDeleteView.as_view(),
        name="services-delete",
    ),
    path(
        "services/edit/<int:pk>",
        service_views.ServiceUpdateView.as_view(),
        name="services-edit",
    ),
    path("ads/", ad_company_views.AdCompanyListView.as_view(), name="ads-list"),
    path("clients/", client_views.ClientListView.as_view(), name="clients-list"),
    path(
        "clients/active",
        client_views.ActiveClientListView.as_view(),
        name="active-client-list",
    ),
    path(
        "contracts/", contract_views.ContractListView.as_view(), name="contracts-list"
    ),
]
