from datetime import date
from decimal import Decimal
from django.test import TestCase

from spendings import models


class TestSpendingsView(TestCase):
    def setUp(self) -> None:
        self.category = models.Category.objects.create(name="fun")
        self.account = models.Account.objects.create(name="foo")
        self.spending_1 = models.Spending.objects.create(
            date_spent=date.fromisoformat("2023-01-11"),
            amount_spent=Decimal(11.5),
            description="cinema",
            category=self.category,
            account=self.account,
        )
        self.spending_2 = models.Spending.objects.create(
            date_spent=date.fromisoformat("2023-01-10"),
            amount_spent=Decimal(1.5),
            description="newspaper",
            category=self.category,
            account=self.account,
        )

    def test_spendings_index(self) -> None:
        response = self.client.get("/spendings/")
        content = response.content.decode()
        spendings = sorted(
            [self.spending_1, self.spending_2], key=lambda s: s.date_spent
        )
        expected_content = [
            f"{s.date_spent}-{s.description}-{s.amount_spent:.2f}-{s.category.name}"
            for s in spendings
        ]
        for ec in expected_content:
            self.assertIn(ec, content)
