# Generated by Django 4.2 on 2023-04-23 19:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="details",
            field=models.TextField(),
        ),
    ]
