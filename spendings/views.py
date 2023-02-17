from django.shortcuts import render

from . import models


def index(request):
    spendings = models.Spending.objects.order_by("date_spent")
    context = {"spending_list": spendings}
    return render(request, "spendings/index.html", context)
