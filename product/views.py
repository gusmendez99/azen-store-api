from django.core.exceptions import PermissionDenied
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from category.models import Category
from category.serializers import CategorySerializer
from permission.services import APIPermissionClassFactory
from product.models import Product
from product.serializers import ProductSerializer

""" def evaluate_user(user, obj, request):
    return user.username == obj.parent.username """
      
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='ProductPermission',
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
                    'categories': lambda user, obj, req: user.is_authenticated,
                    'perform_create': lambda user, obj, req: user.is_authenticated,
                }
            }
        ),
    )

    # POST method
    def perform_create(self, serializer):
        user = self.request.user
        product = serializer.save()
        assign_perm('product.change_product', user, product)
        assign_perm('product.view_product', user, product)
        return Response(serializer.data)

    # GET method
    @action(detail=True, methods=['get'])
    def categories(self, request, pk=None):
        product = self.get_object()
        queryset = product.categories.all()
        data = CategorySerializer(queryset, many = True).data
        return Response(data)
