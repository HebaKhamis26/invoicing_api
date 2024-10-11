from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from invoices.models import Invoice

class InvoiceExchangeRate(generics.RetrieveAPIView):
    queryset = Invoice.objects.all()
    def get(self, request, *args, **kwargs):
        invoice = self.get_object()
        return Response({"id": invoice.id, "invoice_exchange_rate": invoice.exchange_rate}, status=status.HTTP_200_OK)

