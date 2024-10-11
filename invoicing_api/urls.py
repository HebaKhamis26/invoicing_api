# multi_currency_invoice/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from invoices.views import InvoiceViewSet
from analytics.views import TotalRevenueView, AverageInvoiceView
from currency.views import InvoiceExchangeRate

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # This will include the Invoice URLs
    path('api/analytics/revenue/', TotalRevenueView.as_view(), name='analytics-revenue'),
    path('api/analytics/average/', AverageInvoiceView.as_view(), name='analytics-average'),
    path('api/currency/<int:pk>/exchange/', InvoiceExchangeRate.as_view(), name='exchange-rate'),
]