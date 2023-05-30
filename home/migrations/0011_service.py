# Generated by Django 4.2 on 2023-05-04 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0010_contactmessage_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("title", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=255)),
            ],
        ),
    ]