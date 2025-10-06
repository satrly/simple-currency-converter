from currency.converter import CurrencyConverter

def main():
    converter = CurrencyConverter()

    print("=== Конвертер валют ===")
    print("Поддерживаемые валюты:", ", ".join(converter.rates.keys()))
    print("Пример ввода: 100 usd eur")
    print("Введите 'exit' для выхода")

    while True:
        user_input = input("\nВведите сумму и валюты: ").strip()
        if user_input.lower() == "exit":
            print("Выход...")
            break

        parts = user_input.split()
        if len(parts) != 3:
            print("Неправильный формат. Используйте: <сумма> <из валюты> <в валюту>")
            continue

        try:
            amount = float(parts[0])
            from_currency = parts[1]
            to_currency = parts[2]

            result = converter.convert(amount, from_currency, to_currency)
            print(f"{amount} {from_currency.upper()} = {result} {to_currency.upper()}")
        except ValueError as e:
            print("Ошибка:", e)
        except Exception as e:
            print("Что-то пошло не так:", e)

if __name__ == "__main__":
    main()
