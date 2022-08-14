from django.urls import path
from .views import ExpenseListView, ExpenseUpdateView, ExpenseDeleteView


urlpatterns = [
    path('', ExpenseListView.as_view(), name = 'Expense-list-view'),
    path('expense-update/<int:pk>/', ExpenseUpdateView.as_view(), name = 'Expense-update-view'),
    path('expense-delete-confirmation/<int:pk>/', ExpenseDeleteView.as_view(), name = 'Expense-delete-confirmation-view')
]