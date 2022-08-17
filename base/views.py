from .models import Expense
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    fields = '__all__'
    template_name = 'base/login.html'
    redirect_authenticated_user = True
    LoginView.next_page = reverse_lazy('Expense-list-view')
    
class UserLogoutView(LogoutView):
    next_page = 'Expense-login-view'

class ExpenseListView(LoginRequiredMixin, CreateView, ListView):
    model = Expense
    fields = '__all__'
    template_name = 'base/expense.html'
    success_url = reverse_lazy('Expense-list-view')

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = '__all__'
    success_url = reverse_lazy('Expense-list-view')

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    context_object_name = 'expense'
    success_url = reverse_lazy('Expense-list-view')
    




