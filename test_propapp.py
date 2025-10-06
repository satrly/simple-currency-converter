
import unittest
from .probapp import convert_currency, EXCHANGE_RATES

class TestCurrencyConverter(unittest.TestCase):

    def test_usd_to_eur(self):
        amount = 100
        from_currency = "USD"
        to_currency = "EUR"
    
        result = convert_currency(amount, from_currency, to_currency)
        
        expected = round(amount * EXCHANGE_RATES[to_currency] / EXCHANGE_RATES[from_currency], 2)
        self.assertEqual(result, expected)

    def test_rub_to_usd(self):
       
        amount = 8300
        from_currency = "RUB"
        to_currency = "USD"
        
        result = convert_currency(amount, from_currency, to_currency)
        
        expected = round(amount * EXCHANGE_RATES[to_currency] / EXCHANGE_RATES[from_currency], 2)
        self.assertEqual(result, expected)

    def test_same_currency(self):
        
        amount = 500
        from_currency = "CNY"
        to_currency = "CNY"
        
        result = convert_currency(amount, from_currency, to_currency)
        
        self.assertEqual(result, amount)

    def test_invalid_from_currency(self):

        amount = 100
        from_currency = "ABC"
        to_currency = "USD"
        

        with self.assertRaises(ValueError) as context:
            convert_currency(amount, from_currency, to_currency)
        self.assertIn("Неизвестная валюта", str(context.exception))

    def test_invalid_to_currency(self):

        amount = 100
        from_currency = "USD"
        to_currency = "XYZ"
        
        with self.assertRaises(ValueError) as context:
            convert_currency(amount, from_currency, to_currency)
        self.assertIn("Неизвестная валюта", str(context.exception))

if __name__ == "__main__":
    unittest.main()
