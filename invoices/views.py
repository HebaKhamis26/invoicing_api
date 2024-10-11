import requests
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice
from .serializers import InvoiceSerializer
from currency.utils import convert_currency, get_exchange_rate

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def create(self, request, *args, **kwargs):
        # Deserialize the request data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save the invoice
        invoice = serializer.save()

        # Extract currency and amount
        latest_invoice = Invoice.objects.latest('id')
        latest_amount = latest_invoice.amount
        latest_currency = latest_invoice.currency

        # Convert to standard currency (USD)
        amount_in_usd = convert_currency(latest_amount, latest_currency)

        # Get Exchange Rate
        exchange_rate = get_exchange_rate(latest_currency)

        # Save the amount_in_usd and the exchange_rate
        latest_invoice.amount_in_usd = amount_in_usd
        latest_invoice.exchange_rate = exchange_rate
        latest_invoice.save()

        return Response(InvoiceSerializer(invoice).data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)