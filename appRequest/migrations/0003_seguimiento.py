# Generated by Django 4.1 on 2023-08-11 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("appRequest", "0002_solicitudes_usuario"),
    ]

    operations = [
        migrations.CreateModel(
            name="Seguimiento",
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
                ("area", models.CharField(max_length=100)),
                ("comentario", models.CharField(max_length=500)),
                (
                    "id_solicitud",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appRequest.solicitudes",
                    ),
                ),
            ],
        ),
    ]