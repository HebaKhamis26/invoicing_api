from rest_framework import serializers
from .models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['customer', 'amount', 'currency', 'amount_in_usd', 'exchange_rate', 'invoice_date']
