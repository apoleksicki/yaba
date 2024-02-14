from decimal import Decimal

from django.db import models
from django.db.models import QuerySet


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)


class Account(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)

    @property
    def balance(self) -> Decimal:
        transactions = Transaction.objects.filter(account=self)
        return sum([t.amount_spent for t in transactions])


class Transaction(models.Model):
    date_spent = models.DateField("date created")
    amount_spent = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.date_spent}-{self.description}-{self.amount_spent:.2f}-{self.category}"


class Budget(models.Model):
    begins_on = models.DateField()
    ends_on = models.DateField()
    created_at = models.DateTimeField(auto_now=True)

    @property
    def transactions(self) -> QuerySet[Transaction]:
        return Transaction.objects.filter(
            date_spent__gte=self.begins_on, date_spent__lte=self.ends_on
        )
