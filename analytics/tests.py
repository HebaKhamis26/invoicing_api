from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from invoices.models import Invoice

class AnalyticsViewTest(APITestCase):

    def setUp(self):
        # Create sample invoices
        Invoice.objects.create(customer="John", amount=100, currency="USD", amount_in_usd=100)
        Invoice.objects.create(customer="Jane", amount=200, currency="USD", amount_in_usd=200)

    def test_get_revenue(self):
        """
        Test that the revenue analytics API returns the correct data.
        """
        url = reverse('analytics-revenue')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the response data
        self.assertEqual(response.data['total_revenue_usd'], 300)

    def test_get_average(self):
        """
        Test that the average analytics API returns the correct data.
        """
        url = reverse('analytics-average')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check the response data
        self.assertEqual(response.data['average_invoice_size_usd'], 150)