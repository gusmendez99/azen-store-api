from django.db import models
from django.conf import settings
from product.models import Product
from django.utils.timezone import now

class GalleryItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )
    image = models.ImageField(max_length=255, null=True, blank=True, upload_to="uploads/gallery/")
    created_at = models.DateField(default=now)

    def __str__(self):
        return "Image of product {0}".format(self.product)
