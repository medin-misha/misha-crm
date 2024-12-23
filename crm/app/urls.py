from django.urls import path
from .views import UsersIndexView, ServiceListView

app_name = "app"

urlpatterns = [
    path("", UsersIndexView.as_view(), name="user-index"),

    path("products/", ServiceListView.as_view(), name="servises-list"),

]
