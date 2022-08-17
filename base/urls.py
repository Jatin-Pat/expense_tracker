from django.urls import path
from .views import ExpenseListView, ExpenseUpdateView, ExpenseDeleteView, UserLoginView, UserLogoutView, UserRegisterForm, ExpenseSearchView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name = 'Expense-login-view'),
    path('logout/', UserLogoutView.as_view(), name = 'Expense-logout-view'),
    path('register/', UserRegisterForm.as_view(), name = 'Expense-register-view'),
    path('', ExpenseListView.as_view(), name = 'Expense-list-view'),
    path('search/', ExpenseSearchView.as_view(), name = 'Expense-search-view'),
    path('expense-update/<int:pk>/', ExpenseUpdateView.as_view(), name = 'Expense-update-view'),
    path('expense-delete-confirmation/<int:pk>/', ExpenseDeleteView.as_view(), name = 'Expense-delete-confirmation-view')
]