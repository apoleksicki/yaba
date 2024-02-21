from django.contrib import admin

from .models import Account, Estimate
from .models import Category
from .models import Transaction
from .models import Budget


class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 1


class AccountAdmin(admin.ModelAdmin):
    inlines = [TransactionInline]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [TransactionInline]


class EstimateInline(admin.TabularInline):
    model = Estimate


class BudgetAdmin(admin.ModelAdmin):
    inlines = [EstimateInline]


admin.site.register(Account, AccountAdmin)
admin.site.register(Category, AccountAdmin)
admin.site.register(Transaction)
admin.site.register(Budget, BudgetAdmin)
