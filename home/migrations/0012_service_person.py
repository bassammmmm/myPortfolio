# Generated by Django 4.2 on 2023-05-04 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0011_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="person",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="home.person"
            ),
        ),
    ]
