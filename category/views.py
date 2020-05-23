from django.core.exceptions import PermissionDenied
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from category.models import Category
from product.models import Product
from category.serializers import CategorySerializer
from product.serializers import ProductSerializer
from permission.services import APIPermissionClassFactory

""" def evaluate_user(user, obj, request):
    return user.username == obj.parent.username """
      
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='CategoryPermission',
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

    # POST method
    def perform_create(self, serializer):
        user = self.request.user
        category = serializer.save()
        assign_perm('category.change_category', user, category)
        assign_perm('category.view_category', user, category)
        return Response(serializer.data)

    # GET method
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        queryset = Product.objects.filter(categories__id = category.id)
        data = ProductSerializer(queryset, many = True).data
        return Response(data)
