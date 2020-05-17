from rest_framework import serializers
from category.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'user',
            'is_ordered',
            'created_at',
            'products'
        )
