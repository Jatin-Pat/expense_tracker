from django.shortcuts import render
from .models import Expense
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class ExpenseListView(ListView):
    model = Expense

class ExpenseDetailView(DetailView):
    model = Expense

