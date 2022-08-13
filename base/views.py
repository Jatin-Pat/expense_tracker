from django.shortcuts import render
from .models import Expense
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

class ExpenseListView(ListView):
    object = Expense

class ExpenseDetailView(DetailView):
    object = Expense

class ExpenseCreateView(CreateView):
    object = Expense
    fields = '__all__'
    success_url = reverse_lazy('expense')
