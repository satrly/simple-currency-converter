import pytest
from probapp import convert_currency, EXCHANGE_RATES, main



def test_usd_to_eur():
    assert convert_currency(100, "USD", "EUR") == 85.0

def test_rub_to_usd():
    assert convert_currency(8300, "RUB", "USD") == 100.0

def test_same_currency():
    assert convert_currency(500, "CNY", "CNY") == 500

def test_invalid_from_currency():
    with pytest.raises(ValueError):
        convert_currency(100, "ABC", "USD")

def test_invalid_to_currency():
    with pytest.raises(ValueError):
        convert_currency(100, "USD", "XYZ")




def test_main_valid(monkeypatch, capsys):
    inputs = iter(['100', 'USD', 'EUR'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert '100.0 USD = 85.0 EUR' in captured.out

def test_main_invalid_from(monkeypatch, capsys):
    inputs = iter(['100', 'ABC', 'EUR'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert 'Неизвестная валюта' in captured.out

def test_main_invalid_to(monkeypatch, capsys):
    inputs = iter(['100', 'USD', 'XYZ'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert 'Неизвестная валюта' in captured.out
