from django.core.exceptions import PermissionDenied
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from invoice.models import Invoice
from order.models import Order
from invoice.serializers import InvoiceSerializer
from permission.services import APIPermissionClassFactory

""" def evaluate_user(user, obj, request):
    return user.username == obj.parent.username """
      
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='InvoicePermission',
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
        queryset = Invoice.objects.all()
        user_id = self.request.query_params.get('user', None)
        if user_id is not None:
            orders = Order.objects.filter(user__id=user_id)
            queryset = queryset.filter(order__in=orders)
        return queryset

    # POST method
    def perform_create(self, serializer):
        user = self.request.user
        invoice = serializer.save()
        assign_perm('invoice.change_invoice', user, invoice)
        assign_perm('invoice.view_invoice', user, invoice)
        return Response(serializer.data)
