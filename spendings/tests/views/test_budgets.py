import datetime

from django.test import TestCase

from spendings import models


class TestBudgetsView(TestCase):
    def setUp(self) -> None:
        self.budget_1 = models.Budget.objects.create(
            begins_on=datetime.date(2024, 1, 1),
            ends_on=datetime.date(2024, 1, 31),
        )

        self.budget_2 = models.Budget.objects.create(
            begins_on=datetime.date(2024, 2, 1),
            ends_on=datetime.date(2024, 2, 29),
        )

    def test_budgets_returns_list_of_budgets_on_get(self) -> None:
        response = self.client.get("/spendings/budgets/")
        self.assertEqual(200, response.status_code)
        content = response.content.decode()
        self.assertIn(str(self.budget_1), content)
        self.assertIn(str(self.budget_2), content)
