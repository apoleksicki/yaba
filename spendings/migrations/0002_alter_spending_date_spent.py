# Generated by Django 4.1.5 on 2023-01-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("spendings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="spending",
            name="date_spent",
            field=models.DateField(verbose_name="date spent"),
        ),
    ]
