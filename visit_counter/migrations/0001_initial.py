# Generated by Django 4.2.4 on 2023-08-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Visit",
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
                ("count", models.PositiveIntegerField(default=0)),
            ],
            options={
                "verbose_name": "Visit",
                "verbose_name_plural": "Visits",
            },
        ),
    ]
