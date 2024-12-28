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
    path("login/", user_views.UserLoginView.as_view(), name="user-login"),
    path("logout/", user_views.UserLogoutView.as_view(), name="user-logout"),
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
    path("clients/", client_views.ClientListView.as_view(), name="clients-list"),
    path(
        "clients/active",
        client_views.ActiveClientListView.as_view(),
        name="active-client-list",
    ),
    path(
        "clients/new/", client_views.ClientCreateView.as_view(), name="clients-create"
    ),
    path(
        "clients/edit/<int:pk>",
        client_views.ClientUpdateView.as_view(),
        name="clients-edit",
    ),
    path(
        "clients/detail/<int:pk>",
        client_views.ClientDetailView.as_view(),
        name="clients-detail",
    ),
    path(
        "clients/delete/<int:pk>",
        client_views.ClientDeleteView.as_view(),
        name="clients-delete",
    ),
    path(
        "contracts/", contract_views.ContractListView.as_view(), name="contracts-list"
    ),
    path(
        "contracts/new/",
        contract_views.ContractCreateView.as_view(),
        name="contracts-create",
    ),
    path(
        "contracts/detail/<int:pk>",
        contract_views.ContractDetailView.as_view(),
        name="contracts-detail",
    ),
    path(
        "contracts/edit/<int:pk>",
        contract_views.ContractUpdateView.as_view(),
        name="contracts-edit",
    ),
    path(
        "contracts/delete/<int:pk>",
        contract_views.ContractDeleteView.as_view(),
        name="contracts-delete",
    ),

    path("ads/", ad_company_views.AdCompanyListView.as_view(), name="ads-list"),
    path("ads/new/", ad_company_views.AdCompanyCreateView.as_view(), name="ads-create"),
    path("ads/detail/<int:pk>", ad_company_views.AdCompanyDetailView.as_view(), name="ads-detail"),
    path("ads/edit/<int:pk>", ad_company_views.AdCompanyUpdateView.as_view(), name="ads-edit"),
    path("ads/delete/<int:pk>", ad_company_views.AdCompanyDeleteView.as_view(), name="ads-delete"),
    path("ads/statistic/", ad_company_views.AdCompanyStatisticView.as_view(), name="ads-statistic"),
]
