from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("budgets/", views.budgets, name="budgets"),
]
