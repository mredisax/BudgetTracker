from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.decorators.http import require_POST
from .models import Transaction, Account, TransactionCategory, TransactionTag
from .forms import TransactionForm, TagForm, CategoryForm


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
            print(transaction.account)
            transaction.save()
            form.save_m2m()
            return redirect('transaction_detail', pk=transaction.pk)
        else:
            print("no valid")
        return render(request, self.template_name, {'form': form, 'action': 'create'})

class TransactionEditView(View):
    template_name = 'budget/transaction_form.html'

    # @login_required
    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        form = TransactionForm(self.request.user, instance=transaction)
        return render(request, self.template_name, {'form': form, 'action': 'edit'})

    # @login_required
    @require_POST
    def post(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        form = TransactionForm(request.user, request.POST, instance=transaction)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.owner = form.cleaned_data['account']
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