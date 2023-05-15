from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.decorators.http import require_POST
from .models import Transaction, Account, TransactionCategory, TransactionTag
from .forms import TransactionForm


class TransactionListView(LoginRequiredMixin, View):
    template_name = 'budget/transaction_list.html'
    context_object_name = 'transactions'
    login_url = "/admin"


    def get(self, request):        
        transactions = Transaction.objects.filter(
            account__owner=self.request.user
            ).prefetch_related('tags')
        return render(request, self.template_name, {'transactions': transactions})


class TransactionDetailView(View):
    template_name = 'budget/transaction_detail.html'

    # @login_required
    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        return render(request, self.template_name, {'transaction': transaction})


class TransactionCreateView(View):
    template_name = 'budget/transaction_form.html'

    # @login_required
    def get(self, request):
        form = TransactionForm(request.user)
        return render(request, self.template_name, {'form': form, 'action': 'Create'})

    # @login_required
    def post(self, request):
        form = TransactionForm(request.user, request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            new_category_name = form.cleaned_data.get('new_category')
            if new_category_name:
                new_category = TransactionCategory.objects.create(name=new_category_name)
                transaction.category = new_category
            else:
                transaction.category = form.cleaned_data['category']
            transaction.account = form.cleaned_data['account']  
            transaction.owner = request.user
            transaction.save()
            form.save_m2m()
            return redirect('transaction_detail', pk=transaction.pk)
        return render(request, self.template_name, {'form': form, 'action': 'Create'})


class TransactionEditView(View):
    template_name = 'budget/transaction_form.html'

    # @login_required
    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        form = TransactionForm(self.request.user, instance=transaction)
        return render(request, self.template_name, {'form': form, 'action': 'Edit'})

    # @login_required
    def post(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        form = TransactionForm(request.user, request.POST, instance=transaction)
        if form.is_valid():
            transaction = form.save(commit=False)
            # transaction.owner = form.cleaned_data['account']
            transaction.category = form.cleaned_data['category']
            transaction.save()
            form.save_m2m()
            return redirect('transaction_detail', pk=transaction.pk)
        return render(request, self.template_name, {'form': form, 'action': 'Edit'})


class TransactionDeleteView(View):
    # @login_required
    @require_POST
    def post(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        transaction.delete()
        return redirect('transaction_list')
