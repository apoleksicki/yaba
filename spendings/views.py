from django.http import HttpResponse

from . import models


def index(request):
    spendings = models.Spending.objects.order_by("date_spent")
    response_content = "\n".join(
        [
            f"{s.date_spent}, {s.description}, {s.amount_spent}, {s.category.name}"
            for s in spendings
        ]
    )
    return HttpResponse(response_content)
