# Generated by Django 5.1.4 on 2024-12-27 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_adcompany_service_alter_client_ad_company"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="ad_company",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="clients",
                to="app.adcompany",
            ),
        ),
    ]
