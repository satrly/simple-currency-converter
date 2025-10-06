import logging
from converter.cache import Cache


class CurrencyConverter:
    def __init__(self, rates=None):
        self.rates = rates or {
            "USD": 1.0,
            "EUR": 0.93,
            "GBP": 0.80,
            "JPY": 150.1,
            "CNY": 7.25,
            "AUD": 1.56,
            "CAD": 1.38,
            "RUB": 98.0
        }
        self.cache = Cache(ttl=10)

    def update_rates(self, new_rates: dict):
        """Обновляет существующие курсы валют."""
        self.rates.update(new_rates)
        self.logger.info("Курсы валют обновлены.")

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """Конвертирует сумму между валютами с использованием кеша."""
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Одна из валют не поддерживается")

        cache_key = f"{from_currency}_{to_currency}"
        rate = self.cache.get(cache_key)

        if rate is not None:
            self.logger.debug(f"Курс {from_currency}->{to_currency} взят из кеша")
        else:
            rate = self.rates[to_currency] / self.rates[from_currency]
            self.cache.set(cache_key, rate)
            self.logger.debug(f"Курс {from_currency}->{to_currency} сохранён в кеш")

        result = amount * rate
        return round(result, 2)  
