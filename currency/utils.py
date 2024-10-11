import requests
from django.conf import settings
from decimal import Decimal

def convert_currency(amount, from_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    json_response = response.json()
    rates = json_response.get('rates', {})
    rate = rates[from_currency]
    converted_amount = amount / Decimal(rate)
    return converted_amount

def get_exchange_rate(from_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    json_response = response.json()
    rates = json_response.get('rates', {})
    rate = rates[from_currency]
    return rate
