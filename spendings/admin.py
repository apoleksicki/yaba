from django.contrib import admin

from .models import Account
from .models import Category
from .models import Transaction
from .models import Budget

admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Budget)
