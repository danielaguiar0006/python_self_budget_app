class FinanceData:
    def __init__(
        self, total_balance=0, monthly_income=None, monthly_expenses=None, savings=None
    ):
        self.total_balance = total_balance
        self.monthly_income = monthly_income or {}
        self.monthly_expenses = monthly_expenses or {}
        self.savings = savings or {}

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

    def to_dict(self):
        return {
            "total_balance": self.total_balance,
            "monthly_income": self.monthly_income,
            "monthly_expenses": self.monthly_expenses,
            "savings": self.savings,
        }
