class FinanceData:
    def __init__(self):
        self.total_balance = 0.00
        self.monthly_income = []
        self.monthly_expenses = []
        self.savings = []

    def update(self, data):
        self.total_balance = float(data["total_balance"])
        self.monthly_income = [
            {key: value} for key, value in data["monthly_income"].items()
        ]
        self.monthly_expenses = [
            {key: value} for key, value in data["monthly_expenses"].items()
        ]
        self.savings = [{key: value} for key, value in data["savings"].items()]

    def add_totals(self, list_of_dicts):
        total = 0
        for dict in list_of_dicts:
            for key, value in dict.items():
                total += value
        return total
