from django.contrib import admin
from .models import Service, AdCompany, Client, Contract
# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = "name", "price"
    list_display_links = list_display


@admin.register(AdCompany)
class AdCompanyAdmin(admin.ModelAdmin):
    list_display = "name", "service", "budget", "promotional_channel"
    list_display_links = list_display


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = "full_name", "email", "phone", "is_active", "ad_company"
    list_display_links = list_display


@admin.register(Contract)
class ServiceAdmin(admin.ModelAdmin):
    list_display = "name", "service", "conclusion_date", "price", "client"
    list_display_links = list_display


