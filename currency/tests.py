import requests
from unittest import mock
from decimal import Decimal
from django.test import TestCase
from .utils import convert_currency, get_exchange_rate

class CurrencyConversionTests(TestCase):

    @mock.patch('currency.utils.requests.get') 
    def test_convert_currency(self, mock_get):
        """
        Test that the converted amount is as expected.
        """
        mock_response = {
            'rates': {
                'EGP': 30.50,
            }
        }
        mock_get.return_value.json.return_value = mock_response

        amount = Decimal('100')
        from_currency = 'EGP'
        expected_converted_amount = amount / Decimal('30.50')

        converted_amount = convert_currency(amount, from_currency)

        self.assertEqual(converted_amount, expected_converted_amount)

    @mock.patch('currency.utils.requests.get')
    def test_get_exchange_rate(self, mock_get):
        """
        Test that the rate returned is as expected.
        """
        mock_response = {
            'rates': {
                'EUR': 0.85,
            }
        }
        mock_get.return_value.json.return_value = mock_response

        from_currency = 'EUR'
        expected_rate = 0.85

        rate = get_exchange_rate(from_currency)

        self.assertEqual(rate, expected_rate)
