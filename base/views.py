from unicodedata import category
from .models import Expense
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.db.models import Q

class UserLoginView(LoginView):
    fields = '__all__'
    template_name = 'base/login.html'
    redirect_authenticated_user = True
    LoginView.next_page = reverse_lazy('Expense-list-view')
    
class UserLogoutView(LogoutView):
    next_page = 'Expense-login-view'

class UserRegisterForm(FormView):
    form_class = UserCreationForm
    template_name = 'base/register.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('Expense-list-view')

    def form_valid(self, form):
        user = form.save() 
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

class ExpenseListView(LoginRequiredMixin, CreateView, ListView):
    model = Expense
    fields = ['category', 'sub_category', 'amount']
    template_name = 'base/expense.html'
    success_url = reverse_lazy('Expense-list-view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].filter(user=self.request.user)
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ExpenseSearchView(ListView):
    model = Expense
    template_name = 'base/search_result.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Expense.objects.filter(
            Q(category__icontains=query) | Q(sub_category__icontains=query)
        )
        return object_list

class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = ['category', 'sub_category', 'amount']
    success_url = reverse_lazy('Expense-list-view')

class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = Expense
    context_object_name = 'expense'
    success_url = reverse_lazy('Expense-list-view')
    




