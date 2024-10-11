# Generated by Django 5.1.1 on 2024-10-10 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0005_invoice_amount_in_usd'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='exchange_rate',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
