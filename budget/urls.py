from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    BudgetView,
    TransactionListView,
    TransactionDetailView,
    TransactionCreateView,
    TransactionEditView,
    TransactionDeleteView,
    TagCreateView,
    CategoryCreateView,
    BudgetCreateView,
)

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction_list'),
    path('budget/<int:budget_id>/', BudgetView.as_view(), name='budget_detail'),
    path('<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('<int:pk>/edit/', TransactionEditView.as_view(), name='transaction_edit'),
    path('<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('tag/add/', TagCreateView.as_view(), name='add_tag'),
    path('category/add/', CategoryCreateView.as_view(), name='add_category'),
    path('budget/add/', BudgetCreateView.as_view(), name='add_budget'),
]
