from datetime import date
from collections import defaultdict
# Singleton decorator
def singleton(class_):
    instances = {}

    def wrapper(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return wrapper

@singleton
class Statistics:
    def __init__(self, transactions):
        self.transactions = transactions
        self.now = date.today()

    def calculate_total_amount(self):
        total_amount = sum(transaction.amount for transaction in self.transactions)
        print(total_amount)
        return total_amount

    def calculate_monthly_amounts(self):
        monthly_amounts = 0
        for transaction in self.transactions:
            print(transaction)
            if transaction.created_at.month == self.now.month:
                monthly_amounts += transaction.amount
        print(monthly_amounts)
        return monthly_amounts or 0.0

    def calculate_daily_amounts(self):
        daily_amounts = 0
        for transaction in self.transactions:
            if transaction.created_at.day == self.now.day:
                daily_amounts += transaction.amount
        return daily_amounts or 0.0

