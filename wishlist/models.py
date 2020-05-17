from django.db import models
from django.conf import settings
from product.models import Product

# Create your models here.
class Wishlist(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        blank=True, null=True, 
        related_name='wishlist',
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.name

class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)   

