from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from rest_framework_jwt.views import (
#    obtain_jwt_token,
    refresh_jwt_token
)

from category.views import CategoryViewSet
from product.views import ProductViewSet
from cart.views import CartViewSet, CartItemViewSet
from . import views

router = routers.DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/', include('rest_auth.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/token-refresh/', refresh_jwt_token),
    url(r'^api/v1/auth/facebook/$', views.FacebookLogin.as_view(), name='fb_login')
]
