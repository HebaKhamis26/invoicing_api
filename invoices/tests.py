from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Invoice

class InvoiceModelTest(TestCase):

    def setUp(self):
        self.invoice = Invoice.objects.create(
            customer="John",
            amount=100,
            currency="EGP",
        )

    def test_invoice_creation(self):
        """Test that an invoice is correctly created"""
        self.assertEqual(self.invoice.customer, "John")
        self.assertEqual(self.invoice.amount, 100)
        self.assertEqual(self.invoice.currency, "EGP")
        self.assertIsNone(self.invoice.amount_in_usd)

    def test_invoice_str(self):
        """Test the string representation of the invoice"""
        self.assertEqual(str(self.invoice), f"Invoice {self.invoice.id} - John - 100 EGP")

class InvoiceAPITests(APITestCase):
    def setUp(self):
        # Sample invoice data
        self.invoice_data = {"customer": "Gigi",
                             "amount": 500,
                             "currency": "EGP",
                             "invoice_date": "2024-10-10"}

        # Create an invoice object for update/delete tests
        self.invoice = Invoice.objects.create(
            customer="Gigi",
            amount=500,
            currency="EUR",
            invoice_date="2024-10-10")

    def test_create_invoice(self):
        """
        Test creating a new invoice using POST
        """
        url = reverse('invoice-list')  # URL for creating an invoice
        response = self.client.post(url, self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_invoice_list(self):
        """
        Test retrieving the list of invoices using GET
        """
        url = reverse('invoice-list')  # URL for retrieving invoice list
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure there's only one invoice

    def test_retrieve_specific_invoice(self):
        """
        Test retrieving a specific invoice by its ID
        """
        url = reverse('invoice-detail', kwargs={'pk': self.invoice.id})  # URL for retrieving a specific invoice
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['amount'], '500.00')

    def test_update_invoice(self):
        """
        Test updating an invoice using PUT
        """
        url = reverse('invoice-detail', kwargs={'pk': self.invoice.id})  # URL for updating an invoice
        updated_data = self.invoice_data
        updated_data['amount'] = 200
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['amount'], '200.00')

    def test_delete_invoice(self):
        """
        Test deleting an invoice using DELETE
        """
        url = reverse('invoice-detail', kwargs={'pk': self.invoice.id})  # URL for deleting an invoice
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)