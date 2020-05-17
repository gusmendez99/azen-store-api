from django.db import models
from category.models import Category
from decimal import Decimal
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, null=False)
    category = models.ManyToManyField(Category, related_name="category_list")
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.01, validators=[MinValueValidator(Decimal('0.01'))])
    stock = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=6, decimal_places=2, default=0.01, validators=[MinValueValidator(Decimal('0.01'))])
    image = models.ImageField(upload_to ='uploads/products/% Y/% m/% d/') 

    def __str__(self):
        return self.name
