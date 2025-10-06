from converter.converter import CurrencyConverter
from converter.cache import SimpleCache

rates = {"USD": 1, "EUR": 0.93, "JPY": 156.12, "RUB": 96.7}

converter = CurrencyConverter(rates)
cache = SimpleCache()

def get_conversion(amount, from_cur, to_cur):
    key = f"{amount}-{from_cur}-{to_cur}"
    cached = cache.get(key)
    if cached:
        print("Из кэша:", cached)
        return cached
    result = converter.convert(amount, from_cur, to_cur)
    cache.set(key, result)
    return result

if __name__ == "__main__":
    print("Пример работы программы:")
    print(get_conversion(100, "USD", "EUR"))
    print(get_conversion(100, "RUB", "EUR"))  
    print(get_conversion(200, "EUR", "JPY"))