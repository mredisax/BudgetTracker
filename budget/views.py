from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.decorators.http import require_POST
from .models import Budget, Transaction, Account, TransactionCategory, TransactionTag
from .forms import TransactionForm, TagForm, CategoryForm, BudgetForm
from .statistics import Statistics
from .budget_factory import HomeBudgetFactory, CompanyBudgetFactory
from datetime import datetime

class BudgetView(View):
    template_name = 'budget/budget_detail.html'

    def get(self, request, budget_id):
        budget = Budget.objects.get(id=budget_id)
        context = {
            'budget': budget,
        }
        return render(request, self.template_name, context)

class TransactionListView(View):
    template_name = 'budget/transaction_list.html'
    context_object_name = 'transactions'
    login_url = "/admin"

    def get(self, request):        
        transactions = Transaction.objects.filter(
            account__owner=self.request.user
            ).prefetch_related('tags')

        statistics = Statistics(transactions)
        total_amount = statistics.calculate_total_amount()
        monthly_amounts = statistics.calculate_monthly_amounts()
        daily_amounts = statistics.calculate_daily_amounts()

        return render(request, self.template_name,
                      {'transactions': transactions,
                        'total_amount': total_amount,
                        'monthly_amounts': monthly_amounts,
                        'daily_amounts': daily_amounts,
                       })

class TransactionDetailView(View):
    template_name = 'budget/transaction_detail.html'

    # @login_required
    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        return render(request, self.template_name, {'transaction': transaction})


class TransactionCreateView(View):
    template_name = 'budget/transaction_form.html'

    def get(self, request):
        form = TransactionForm(self.request.user)
        return render(request, self.template_name, {'form': form, 'action': 'create'})

    # @require_POST
    def post(self, request):
        form = TransactionForm(request.user, request.POST)
        account = Account.objects.get(owner=request.user)
        if form.is_valid():
            print("valid")
            transaction = form.save(commit=False)
            transaction.account = account
            transaction.save()
            form.save_m2m()
            return redirect('transaction_detail', pk=transaction.pk)
        else:
            print("no valid")
        return render(request, self.template_name, {'form': form, 'action': 'create'})

class TransactionEditView(View):
    template_name = 'budget/transaction_form.html'

    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        form = TransactionForm(self.request.user, instance=transaction)
        return render(request, self.template_name, {'form': form, 'action': 'edit'})

    def post(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        form = TransactionForm(request.user, request.POST, instance=transaction)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.category = form.cleaned_data['category']
            transaction.save()
            form.save_m2m()
            return redirect('transaction_detail', pk=transaction.pk)
        return render(request, self.template_name, {'form': form, 'action': 'edit'})

class TransactionDeleteView(View):
    # @login_required
    template_name = 'budget/transaction_confirm_delete.html'
    def get(self, request, pk):
        transaction = Transaction.objects.get(pk=pk)
        return render(request, self.template_name, {'transaction': transaction})
    def post(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        transaction.delete()
        return redirect('transaction_list')


class BudgetCreateView(View):
    template_name = 'budget/transaction_form_budget.html'
    def get(self, request):
        form = BudgetForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget_type = form.cleaned_data['budget_type']
            name = form.cleaned_data['name']
            if budget_type == 'Home':
                factory = HomeBudgetFactory()
            elif budget_type == 'Company':
                factory = CompanyBudgetFactory()
            else:
                raise ValueError('Invalid budget type')

            budget = factory.create_budget(name)
            form.save()
            return redirect('transaction_create')
        return render(request, self.template_name, {'form': form})

class TagCreateView(View):
    template_name = 'budget/transaction_form_tag.html'
    def get(self, request):
        form = TagForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_create')
        return render(request, self.template_name, {'form': form})

class CategoryCreateView(View):
    template_name = 'budget/transaction_form_category.html'
    def get(self, request):
        form = CategoryForm()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_create')
        return render(request, self.template_name, {'form': form})