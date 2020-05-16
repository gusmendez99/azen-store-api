from django.http import HttpResponse
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

def index(request):
    return HttpResponse("<h1>This is the HomePage of Azen Store API. Try it out with Postman or CURL.</h1>")

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter