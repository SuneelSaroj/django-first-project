# Generated by Django 4.2 on 2023-04-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Emp",
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
                ("name", models.CharField(max_length=200)),
                ("emp_id", models.CharField(max_length=200)),
                ("mobile", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=200)),
                ("is_working", models.BooleanField(default=True)),
                ("department", models.CharField(max_length=50)),
            ],
        ),
    ]
