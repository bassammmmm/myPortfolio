# Generated by Django 4.2 on 2023-04-23 19:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_alter_person_details"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="description",
            field=models.CharField(max_length=355),
        ),
    ]