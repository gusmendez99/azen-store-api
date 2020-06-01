from django.core.exceptions import PermissionDenied
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer
from permission.services import APIPermissionClassFactory
from wishlist.models import Wishlist
from wishlist.serializers import WishlistSerializer

""" def evaluate_user(user, obj, request):
    return user.username == obj.parent.username """
      
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='WishlistPermission',
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
                }
            }
        ),
    )

    def get_queryset(self):
        queryset = Wishlist.objects.all()
        user_id = self.request.query_params.get('user', None)
        if user_id is not None:
            queryset = queryset.filter(user__id=user_id)
        return queryset

    # POST method
    def perform_create(self, serializer):
        user = self.request.user
        wishlist = serializer.save()
        assign_perm('wishlist.change_wishlist', user, wishlist)
        assign_perm('wishlist.view_wishlist', user, wishlist)
        return Response(serializer.data)

    # GET method
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        wishlist = self.get_object()
        queryset = wishlist.products.all()
        data = ProductSerializer(queryset, many = True).data
        return Response(data)

    # @action(detail=True, methods=['patch'])
    # def whatever(self, request, pk=None):
    #     wishlist = self.get_object()
    #     # print(wishlist)
    #     # wishlist.products.append(self.request.products)
    #     return Response(WishlistSerializer(wishlist).data)