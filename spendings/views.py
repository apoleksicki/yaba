from django.http import HttpResponse
from django.template import loader

from . import models


def index(request):
    spendings = models.Spending.objects.order_by("date_spent")
    template = loader.get_template('spendings/index.html')
    context = {"spending_list": spendings}
    return HttpResponse(template.render(context, request))
