# Generated by Django 4.2 on 2023-04-25 10:57

from django.db import migrations, models
import home.utils


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_remove_project_detatils_project_details"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMessage",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                ("subject", models.CharField(max_length=250)),
                ("message", models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to=home.utils.project_image_path),
        ),
    ]
