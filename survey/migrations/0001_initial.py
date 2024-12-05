# Generated by Django 5.0.3 on 2024-04-09 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Entry",
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
                (
                    "classification",
                    models.CharField(
                        choices=[
                            ("1", "Group 1"),
                            ("2", "Group 2"),
                            ("3", "Group 3"),
                            ("4", "Group 4"),
                            ("5", "Group 5"),
                            ("6", "Group 6"),
                            ("7", "Group 7"),
                            ("8", "Group 8"),
                            ("9", "Group 9"),
                            ("10", "Group 10"),
                        ],
                        max_length=100,
                    ),
                ),
                ("csection", models.BooleanField(default=False)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="users.userprofile",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Entries",
            },
        ),
    ]