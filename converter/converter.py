class CurrencyConverter:
    def __init__(self, rates):
        if not isinstance(rates, dict):
            raise TypeError("Rates must be a dictionary")
        self.rates = rates

    def convert(self, amount, from_currency, to_currency):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be numeric")
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if from_currency not in self.rates or to_currency not in self.rates:
            raise KeyError("Currency not supported")

        base = amount / self.rates[from_currency]
        result = base * self.rates[to_currency]
        return round(result, 2)