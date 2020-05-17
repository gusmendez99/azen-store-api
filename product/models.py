from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.01, validators=[MinValueValidator(Decimal('0.01'))])
    stock = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2, default=0.01, validators=[MinValueValidator(Decimal('0.01'))])
    featured_image = models.ImageField(upload_to ="uploads/products/% Y/% m/% d/", null=True) 

    categories = models.ManyToManyField('category.Category', related_name="categories")
    
    def __str__(self):
        return self.name
