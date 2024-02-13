from datetime import date
from decimal import Decimal

from django.test import TestCase

from spendings import models


class TestAccount(TestCase):
    def test_balance_property_is_zero_when_no_transactions(self) -> None:
        account = models.Account.objects.create(name="foo")
        self.assertEqual(0, account.balance)

    def test_balance_returns_sum_of_amount_of_all_transactions(self) -> None:
        account = models.Account.objects.create(name="bar")
        category = models.Category.objects.create(name="baz")
        amounts = [Decimal(100), Decimal(-150), Decimal(500)]
        for a in amounts:
            models.Transaction.objects.create(
                date_spent=date.fromisoformat("2023-01-11"),
                amount_spent=a,
                description="cinema",
                category=category,
                account=account,
            )
        self.assertEqual(sum(amounts), account.balance)
