from django.contrib import admin
from .models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "sub_category", "amount", "date")

admin.site.register(Expense, ExpenseAdmin)