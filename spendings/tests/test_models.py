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


class TestBudget(TestCase):
    def test_transactions_returns_empty_list_when_no_transactions(self) -> None:
        budget = models.Budget.objects.create(
            begins_on=date.fromisoformat("2024-02-01"),
            ends_on=date.fromisoformat("2024-02-29"),
        )
        transactions = budget.transactions
        self.assertEqual([], list(transactions))

    def test_transactions_returns_transactions_within_budget_time_frame(self) -> None:
        budget = models.Budget.objects.create(
            begins_on=date.fromisoformat("2024-02-01"),
            ends_on=date.fromisoformat("2024-02-29"),
        )
        account = models.Account.objects.create(name="bar")
        category = models.Category.objects.create(name="baz")

        def build_transaction(date_spent: date) -> models.Transaction:
            return models.Transaction.objects.create(
                date_spent=date_spent,
                amount_spent=Decimal(300),
                description="cinema",
                category=category,
                account=account,
            )

        transactions_within = [
            build_transaction(date.fromisoformat("2024-02-01")),
            build_transaction(date.fromisoformat("2024-02-05")),
            build_transaction(date.fromisoformat("2024-02-07")),
        ]
        dates_outside = [
            date.fromisoformat("2024-01-01"),
            date.fromisoformat("2024-03-05"),
            date.fromisoformat("2024-05-07"),
        ]

        for d in dates_outside:
            build_transaction(d)

        self.assertEqual(transactions_within, list(budget.transactions))
