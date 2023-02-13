from django.db import models


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


class Spending(models.Model):
    date_spent = models.DateField("date spent")
    amount_spent = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.date_spent}-{self.description}-{self.amount_spent}"
