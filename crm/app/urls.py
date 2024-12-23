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
    path("products/", service_views.ServiceListView.as_view(), name="servises-list"),
    path("ads/", ad_company_views.AdCompanyListView.as_view(), name="ads-list"),
    path("leads/", client_views.ClientListView.as_view(), name="leads-list"),
    path(
        "leads/active",
        client_views.ActiveClientListView.as_view(),
        name="active-client-list",
    ),
    path(
        "contracts/", contract_views.ContractListView.as_view(), name="contracts-list"
    ),
]
