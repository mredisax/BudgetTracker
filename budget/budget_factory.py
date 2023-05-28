from .models import Budget, Transaction, Account, TransactionCategory, TransactionTag
class BudgetFactory:
    def create_budget(self, name):
        budget = Budget.objects.create(name=name)
        return budget

class HomeBudgetFactory(BudgetFactory):
    def create_budget(self, name):
        budget = super().create_budget(name)
        # Additional logic specific to home budget
        return budget

class CompanyBudgetFactory(BudgetFactory):
    def create_budget(self, name):
        budget = super().create_budget(name)
        # Additional logic specific to company budget
        return budget