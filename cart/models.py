from django.db import models
from django.conf import settings
from product.models import Product

# Create your models here.
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        blank=True, null=True, 
        related_name='cart',
        on_delete=models.CASCADE
    )
    is_ordered = models.BooleanField(default=False)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)   
