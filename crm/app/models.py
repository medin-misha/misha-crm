from django.db import models
from datetime import date
from .utils.uploads import upload_document


# Create your models here.
class Service(models.Model):
    name: str = models.CharField(max_length=200)
    description: str = models.TextField(max_length=10000, null=True)
    price: float = models.DecimalField(decimal_places=1, max_digits=20)

    class Meta:
        verbose_name = "service"

    def __str__(self):
        return self.name


class AdCompany(models.Model):
    name: str = models.CharField(max_length=200)
    service: Service = models.ForeignKey(to=Service, null=True, on_delete=models.SET_NULL)
    promotional_channel: str = models.CharField(max_length=200, null=True)
    budget: float = models.DecimalField(decimal_places=1, max_digits=20)

    class Meta:
        verbose_name = "ad company"
        verbose_name_plural = "ad companies"

    def __str__(self) -> str:
        return self.name


class Client(models.Model):
    full_name: str = models.CharField(max_length=200)
    phone: int = models.PositiveBigIntegerField()
    email: str = models.EmailField()
    is_active: bool = models.BooleanField(default=False)
    ad_company: AdCompany = models.ForeignKey(to=AdCompany, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = "client"


class Contract(models.Model):
    name: str = models.CharField(max_length=200)
    service: Service = models.ForeignKey(to=Service, on_delete=models.CASCADE)
    document: str = models.FileField(null=True, upload_to=upload_document)
    conclusion_date: date = models.DateField(null=True)
    days_of_action: int = models.PositiveIntegerField(null=True)
    price: float = models.DecimalField(decimal_places=1, max_digits=20)
    client: Client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "contract"

    def __str__(self) -> str:
        return self.name
