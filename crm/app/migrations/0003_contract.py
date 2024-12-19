# Generated by Django 5.1.4 on 2024-12-19 13:30

import app.utils.uploads
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_adcompany"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "document",
                    models.FileField(
                        null=True, upload_to=app.utils.uploads.upload_document
                    ),
                ),
                ("conclusion_date", models.DateField(null=True)),
                ("days_of_action", models.PositiveIntegerField(null=True)),
                ("price", models.DecimalField(decimal_places=1, max_digits=20)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.service"
                    ),
                ),
            ],
            options={
                "verbose_name": "contract",
            },
        ),
    ]