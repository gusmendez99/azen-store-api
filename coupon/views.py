from django.core.exceptions import PermissionDenied
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permission.services import APIPermissionClassFactory
from coupon.models import Coupon
from coupon.serializers import CouponSerializer

""" def evaluate_user(user, obj, request):
    return user.username == obj.parent.username """
      
class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='CouponPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, req: user.is_authenticated,
                    'list': lambda user, req: user.is_authenticated,
                },
                'instance': {
                    'retrieve': lambda user, obj, req: user.is_authenticated,
                    'destroy': lambda user, obj, req: user.is_authenticated,
                    'update': lambda user, obj, req: user.is_authenticated,
                    'partial_update': lambda user, obj, req: user.is_authenticated,
                    'perform_create': lambda user, obj, req: user.is_authenticated,
                }
            }
        ),
    )

    def get_queryset(self):
        queryset = Coupon.objects.all()
        coupon_name = self.request.query_params.get('name', None)
        if coupon_name is not None:
            queryset = queryset.filter(name=coupon_name)
        return queryset

    # POST method
    def perform_create(self, serializer):
        user = self.request.user
        coupon = serializer.save()
        assign_perm('coupon.change_coupon', user, coupon)
        assign_perm('coupon.view_coupon', user, coupon)
        return Response(serializer.data)