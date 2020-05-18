from django.core.exceptions import PermissionDenied
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permission.services import APIPermissionClassFactory
from cart.models import Cart, CartItem
from cart.serializers import CartSerializer, CartItemSerializer
from product.serializers import ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='CartPermission',
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
                    'clear': lambda user, obj, req: user.is_authenticated,
                }
            }
        ),
    )

    # POST method
    def perform_create(self, serializer):
        user = self.request.user
        cart = serializer.save()
        assign_perm('cart.change_cart', user, cart)
        assign_perm('cart.view_cart', user, cart)
        return Response(serializer.data)

    # GET method
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        cart = self.get_object()
        queryset = cart.products.all()
        data = ProductSerializer(queryset, many = True).data
        return Response(data)

    # GET method
    @action(detail=True, methods=['post'])
    def clear(self, request, pk=None):
        cart = self.get_object()
        self.clear_cart(cart)
        cart = self.get_object()
        return Response(CartSerializer(cart).data)

    def clear_cart(self, cart):
        print("Clearing cart...")
        CartItem.objects.filter(cart=cart).delete()
        print ("Cart {} cleared!".format(cart.id))



class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='CartItemPermission',
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
        cart_item = serializer.save()
        assign_perm('cartitem.change_cartitem', user, cart_item)
        assign_perm('cartitem.view_cartitem', user, cart_item)
        return Response(serializer.data)

