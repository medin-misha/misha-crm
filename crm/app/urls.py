from django.urls import path
from .views import UsersIndexView

app_name = "app"

urlpatterns = [
    path("", UsersIndexView.as_view(), name="user-index")
]
