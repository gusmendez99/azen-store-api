from django.core.exceptions import PermissionDenied
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User
from user.serializers import UserSerializer
from permission.services import APIPermissionClassFactory

from cart.models import Cart, CartItem
from cart.serializers import CartItemSerializer
from order.models import Order, OrderItem
from order.serializers import OrderSerializer
from wishlist.models import Wishlist
from wishlist.serializers import WishlistSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='UserPermission',
            permission_configuration={
                'base': {
                    'create': lambda user, req: user.is_superuser,
                    'list': lambda user, req: user.is_authenticated,
                },
                'instance': {
                    'retrieve': lambda user, obj, req: user.is_authenticated,
                    'destroy': lambda user, obj, req: user.is_superuser,
                    'update': lambda user, obj, req: user.is_authenticated,
                    'partial_update': lambda user, obj, req: user.is_authenticated,
                    'perform_create': lambda user, obj, req: user.is_superuser,
                    'cart_items': lambda user, obj, req: user.is_authenticated,
                    'orders': lambda user, obj, req: user.is_authenticated,
                    'wishlist': lambda user, obj, req: user.is_authenticated,
                }
            }
        ),
    )

    @action(detail=True, url_path="cart-items", methods=['get'])
    def cart_items(self, request, pk=None):
        user = self.get_object()
        cart = Cart.objects.filter(user=user).first()

        data = {}
        if cart != None:
            queryset = CartItem.objects.filter(cart=cart).all()
            data = CartItemSerializer(queryset, many=True).data
        
        return Response(data)

    @action(detail=True, methods=['get'])
    def orders(self, request, pk=None):
        user = self.get_object()
        queryset = Order.objects.filter(user=user).all()
        data = OrderSerializer(queryset, many=True).data
        
        return Response(data)   

    
    @action(detail=True, methods=['get'])
    def wishlist(self, request, pk=None):
        user = self.get_object()
        wishlist = Wishlist.objects.filter(user=user).first()
        data = WishlistSerializer(wishlist).data
        
        return Response(data)   
            
