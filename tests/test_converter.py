import pytest
from converter.converter import CurrencyConverter
from converter.cache import SimpleCache

rates = {"USD": 1, "EUR": 0.93, "JPY": 156.12, "RUB": 96.7}
converter = CurrencyConverter(rates)

# === TESTS ===

def test_convert_usd_to_eur():
    result = converter.convert(10, "USD", "EUR")
    assert result == 9.3

def test_invalid_amount_type():
    with pytest.raises(ValueError):
        converter.convert("10", "USD", "EUR")

def test_negative_amount():
    with pytest.raises(ValueError):
        converter.convert(-5, "USD", "EUR")

def test_unsupported_currency():
    with pytest.raises(KeyError):
        converter.convert(10, "USD", "GBP")

def test_cache_store_and_retrieve():
    cache = SimpleCache()
    cache.set("test", 42)
    assert cache.get("test") == 42

def test_cache_clear():
    cache = SimpleCache()
    cache.set("x", 10)
    cache.clear()
    assert cache.get("x") is None