from .models import Budget, Transaction, Account, TransactionCategory, TransactionTag
class BudgetFactory:
    def create_budget(self, budget_type, name):
        if budget_type == "Home":
            return HomeBudget.objects.create(name=name)
        elif budget_type == "Company":
            return CompanyBudget.objects.create(name=name)
        else:
            raise ValueError("Invalid budget type")

class HomeBudget(Budget):
    # Additional fields specific to home budget

    def create_transaction(self, category_name, tags, amount, date):
        category = TransactionCategory.objects.get(name=category_name)
        transaction = Transaction.objects.create(
            budget=self,
            category=category,
            amount=amount,
            date=date
        )
        transaction.tags.add(*tags)
        return transaction

class CompanyBudget(Budget):
    # Additional fields specific to company budget

    def create_transaction(self, category_name, tags, amount, date):
        category = TransactionCategory.objects.get(name=category_name)
        transaction = Transaction.objects.create(
            budget=self,
            category=category,
            amount=amount,
            date=date
        )
        transaction.tags.add(*tags)
        return transaction