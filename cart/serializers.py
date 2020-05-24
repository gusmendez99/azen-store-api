from rest_framework import serializers
from cart.models import Cart, CartItem

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            'id',
            'user',
            'is_ordered',
            'created_at',
            'products'
        )

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        
        fields = (
            'id',
            'cart',
            'quantity',
            'product'
        )
