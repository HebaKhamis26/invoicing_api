# Generated by Django 5.1.1 on 2024-10-10 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_alter_invoice_customer_delete_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='currency',
            field=models.CharField(max_length=3),
        ),
    ]
