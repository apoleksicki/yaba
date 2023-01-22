from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)


class Account(models.Model):
    name = models.CharField(max_length=200)


class Spending(models.Model):
    date_spent = models.DateField("date spent")
    amount_spent = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
