from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now

# Create your models here.
class Coupon(models.Model):
    name = models.CharField(max_length=100, null=False)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.01, validators=[MinValueValidator(Decimal('0.01')), MaxValueValidator(Decimal('99.99'))])
    exp_datetime = models.DateTimeField(default = now)

    def __str__(self):
        return self.name