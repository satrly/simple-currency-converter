
EXCHANGE_RATES = {
    "USD": 1.0,        
    "EUR": 0.92,
    "RUB": 96.5,
    "GBP": 0.82
}

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    if from_currency not in EXCHANGE_RATES:
        raise ValueError(f"Неизвестная валюта: {from_currency}")
    if to_currency not in EXCHANGE_RATES:
        raise ValueError(f"Неизвестная валюта: {to_currency}")
    
    amount_in_usd = amount / EXCHANGE_RATES[from_currency]
    converted_amount = amount_in_usd * EXCHANGE_RATES[to_currency]
    return round(converted_amount, 2)

def main():
    print("Доступные валюты:", ", ".join(EXCHANGE_RATES.keys()))
    
    try:
        amount = float(input("Введите сумму для конвертации: "))
        from_currency = input("Из какой валюты (код): ").upper()
        to_currency = input("В какую валюту (код): ").upper()
        
        result = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {result} {to_currency}")
        
    except ValueError as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    main()