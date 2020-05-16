from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from rest_framework_jwt.views import (
#    obtain_jwt_token,
    refresh_jwt_token
)
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/token-refresh/', refresh_jwt_token),
    url(r'^rest-auth/facebook/$', views.FacebookLogin.as_view(), name='fb_login')
]
