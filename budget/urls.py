from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    TransactionListView,
    TransactionDetailView,
    TransactionCreateView,
    TransactionEditView,
    TransactionDeleteView,
)

urlpatterns = [
    path('', TransactionListView.as_view(), name='transaction_list'),
    path('<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('<int:pk>/edit/', TransactionEditView.as_view(), name='transaction_edit'),
    path('<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
