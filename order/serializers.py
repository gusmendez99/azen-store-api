from rest_framework import serializers
from order.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'delivery_name',
            'delivery_address',
            'details',
            'status',
            'order_date',
            'products'
        )
