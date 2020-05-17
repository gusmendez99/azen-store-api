from rest_framework import serializers
from coupon.models import Coupon

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = (
            'id',
            'name',
            'discount',
            'exp_datetime',
        )
