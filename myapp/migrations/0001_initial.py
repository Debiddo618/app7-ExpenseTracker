# Generated by Django 4.2.6 on 2023-10-24 02:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Expense",
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
                ("date", models.DateField(auto_created=True)),
                ("name", models.CharField(max_length=200)),
                ("amount", models.IntegerField()),
                ("category", models.CharField(max_length=50)),
            ],
        ),
    ]
