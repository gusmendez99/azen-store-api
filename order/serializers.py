from rest_framework import serializers
from order.models import Order, OrderItem

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


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        
        fields = (
            'id',
            'order',
            'quantity',
            'product'
        )
        depth = 1

