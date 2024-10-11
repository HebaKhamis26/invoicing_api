from django.db import models
from datetime import date

class Invoice(models.Model):
    customer = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    amount_in_usd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    invoice_date = models.DateField(default=date.today)

    def __str__(self):
        return f"Invoice {self.id} - {self.customer} - {self.amount} {self.currency}"