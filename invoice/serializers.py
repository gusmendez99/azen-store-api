from rest_framework import serializers
from invoice.models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = (
            'id',
            'order',
            'billing_name',
            'billing_address',
            'billing_ssn',
            'invoice_datetime',
        )
