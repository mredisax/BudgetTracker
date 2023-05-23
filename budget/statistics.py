from abc import ABC, abstractmethod

class Statistics(ABC):
    @abstractmethod
    def calculate(self):
        pass

class BudgetStatistics(Statistics):
    def __init__(self, budget):
        self.budget = budget

    def calculate(self):
        transactions = self.budget.transaction_set.all()
        total_amount = sum(transaction.amount for transaction in transactions)
        return total_amount

class TransactionStatistics(Statistics):
    def __init__(self, transactions):
        self.transactions = transactions

    def calculate(self):
        total_amount = sum(transaction.amount for transaction in self.transactions)
        return total_amount