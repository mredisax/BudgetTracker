from django import forms
from .models import Transaction, TransactionCategory, TransactionTag, Account

class TransactionForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    class Meta:
        model = Transaction
        fields = ['name', 'category', 'account', 'amount','tags']
        widgets = {'tags': forms.CheckboxSelectMultiple}

class TagForm(forms.ModelForm):
    class Meta:
        model = TransactionTag
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = TransactionCategory
        fields = ['name']
