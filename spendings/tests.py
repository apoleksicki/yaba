import os
from django.test import TestCase

from spendings import models


class TestSpendingsView(TestCase):
    def test_spendings_index(self) -> None:
        response = self.client.get("/spendings/")
        self.assertEqual(
            "Hello, world. You're at the spendings index.", response.content.decode()
        )
