# Generated by Django 4.1.5 on 2023-01-08 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("spendings", "0002_alter_spending_date_spent"),
    ]

    operations = [
        migrations.AddField(
            model_name="spending",
            name="amount_spent",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]
