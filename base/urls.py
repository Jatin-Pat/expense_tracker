from django.urls import path
from .views import ExpenseListView, ExpenseDetailView, ExpenseCreateView


urlpatterns = [
    path('', ExpenseListView.as_view(), name = 'Expense-list-view'),
    path('expense/<int:pk>', ExpenseDetailView.as_view(), name = 'Expense-detail-view'),
    path('add-expemse', ExpenseCreateView.as_view(), name = 'Expense-create-view'),
]