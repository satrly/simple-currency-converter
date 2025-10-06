from converter import CurrencyConverter

def main():
    converter = CurrencyConverter()

    print("=== Конвертер валют ===")
    print("Поддерживаемые валюты:", ", ".join(converter.rates.keys()))
    print("Пример: 100 usd eur")

    while True:
        user_input = input("\nВведите сумму и валюты (или 'exit'): ").strip()
        if user_input.lower() == "exit":
            print("Выход...")
            break

        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Формат: <сумма> <из валюты> <в валюту>")
                continue

            amount = float(parts[0])
            from_currency = parts[1].upper()
            to_currency = parts[2].upper()

            result = converter.convert(amount, from_currency, to_currency)
            print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")

        except Exception as e:
            print("Ошибка:", e)


if __name__ == "__main__":
    main()
