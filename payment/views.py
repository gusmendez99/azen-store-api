from django.core.exceptions import PermissionDenied
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from payment.models import Payment
from payment.serializers import PaymentSerializer
from permission.services import APIPermissionClassFactory

""" def evaluate_user(user, obj, request):
    return user.username == obj.parent.username """
      
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='PaymentPermission',
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

    # POST method
    def perform_create(self, serializer):
        user = self.request.user
        payment = serializer.save()
        assign_perm('payment.change_payment', user, payment)
        assign_perm('payment.view_payment', user, payment)
        return Response(serializer.data)
