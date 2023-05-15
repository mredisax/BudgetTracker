from django import forms
from .models import Transaction, TransactionCategory, Account

class TransactionForm(forms.ModelForm):
    new_category = forms.CharField(max_length=100, required=False)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def clean(self):
        cleaned_data = super().clean()
        new_category = cleaned_data.get('new_category')

        if not cleaned_data.get('category') and not new_category:
            raise forms.ValidationError('Please select an existing category or enter a new one.')
        return cleaned_data

    class Meta:
        model = Transaction
        fields = ['name', 'category', 'new_category', 'amount','tags']
        widgets = {'tags': forms.CheckboxSelectMultiple}