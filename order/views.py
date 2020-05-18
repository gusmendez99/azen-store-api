from django.core.exceptions import PermissionDenied
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permission.services import APIPermissionClassFactory
from order.models import Order, OrderItem
from cart.models import Cart, CartItem

from order.serializers import OrderSerializer, OrderItemSerializer
from product.serializers import ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='OrderPermission',
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
                    'products': lambda user, obj, req: user.is_authenticated,
                    'process': lambda user, obj, req: user.is_authenticated,
                }
            }
        ),
    )

    # POST method
    def perform_create(self, serializer):
        user = self.request.user
        cart = Cart.objects.filter(user=user).first()
        order = serializer.save()
        assign_perm('order.change_order', user, order)
        assign_perm('order.view_order', user, order)
        
        if cart != None:
            cart_items = CartItem.objects.filter(cart=cart).all()
            self.create_order_items(order, cart_items, user)
            CartItem.objects.filter(cart=cart).delete()
        
        return Response(serializer.data)
        

    # GET method
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        order = self.get_object()
        queryset = order.products.all()
        data = ProductSerializer(queryset, many = True).data
        return Response(data)

    @action(detail=True, methods=['post'])
    def process(self, request, pk=None):
        order = self.get_object()
        self.change_status(order, 1)
        return Response(OrderSerializer(order).data)

    def create_order_items(self, order, cart_items, user):
        for cart_item in cart_items:
            order_item = OrderItem(
                order = order,
                product = cart_item.product,
                quantity = cart_item.quantity
            )
            order_item.save()
            assign_perm('orderitem.change_orderitem', user, order_item)
            assign_perm('orderitem.view_orderitem', user, order_item)

    def change_status(self, order, status):
        order.status = status
        order.save()
        print ("Order {} processed!".format(order))
            
