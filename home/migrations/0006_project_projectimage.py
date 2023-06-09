# Generated by Django 4.2 on 2023-04-25 07:15

from django.db import migrations, models
import django.db.models.deletion
import home.utils


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_person_skills_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("url", models.CharField(max_length=500)),
                ("completion_date", models.DateField()),
                ("detatils", models.TextField(max_length=500)),
                ("image", models.ImageField(upload_to=home.utils.project_images_path)),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.person"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectImage",
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
                ("image", models.ImageField(upload_to=home.utils.project_images_path)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.project"
                    ),
                ),
            ],
        ),
    ]
