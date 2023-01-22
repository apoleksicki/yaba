from datetime import date
from decimal import Decimal
import os
from django.test import TestCase

from spendings import models


class TestSpendingsView(TestCase):
    def setUp(self) -> None:
        self.category = models.Category.objects.create(name="fun")
        self.spending_1 = models.Spending.objects.create(
            date_spent=date.fromisoformat("2023-01-11"),
            amount_spent=Decimal(11.5),
            description="cinema",
            category=self.category,
        )
        self.spending_2 = models.Spending.objects.create(
            date_spent=date.fromisoformat("2023-01-10"),
            amount_spent=Decimal(1.5),
            description="newspaper",
            category=self.category,
        )

    def test_spendings_index(self) -> None:
        response = self.client.get("/spendings/")
        content = response.content.decode()
        spendings = sorted(
            [self.spending_1, self.spending_2], key=lambda s: s.date_spent
        )
        expected_content = "\n".join(
            [
                f"{s.date_spent}, {s.description}, {'{0:.2}'.format(s.amount_spent)}, {s.category.name}"
                for s in spendings
            ]
        )
        self.assertIn(expected_content, content)
