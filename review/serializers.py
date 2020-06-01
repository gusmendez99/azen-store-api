from rest_framework import serializers
from review.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'product',
            'created_at',
            'rate',
            'content',
            'username'
        )

    def get_username(self, obj):
        return obj.user.username
