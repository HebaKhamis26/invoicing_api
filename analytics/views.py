from django.db.models import Sum, Avg
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from invoices.models import Invoice

class TotalRevenueView(APIView):
    def get(self, request):
        total_revenue = Invoice.objects.aggregate(Sum('amount_in_usd'))['amount_in_usd__sum']
        return Response({"total_revenue_usd": total_revenue}, status=status.HTTP_200_OK)

class AverageInvoiceView(APIView):
    def get(self, request):
        average_invoice_size = Invoice.objects.aggregate(Avg('amount_in_usd'))['amount_in_usd__avg']
        return Response({"average_invoice_size_usd": average_invoice_size}, status=status.HTTP_200_OK)
