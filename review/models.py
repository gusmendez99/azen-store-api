from django.db import models
from django.conf import settings
from product.models import Product
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=False
    )
    content = models.CharField(max_length=1000)
    date = models.DateField(default=now)
    rate = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return "User {0} over {1} with rate {2}".format(self.user, self.product, self.rate)
