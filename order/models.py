from django.conf import settings
from django.utils.timezone import now
from django.db import models
from product.models import Product

class Order(models.Model):    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    delivery_name = models.CharField(max_length=200, null= False)
    delivery_address = models.CharField(max_length=200, null= False)
    details = models.CharField(max_length=255, null= False)
    status = models.PositiveIntegerField()
    order_date = models.DateTimeField(default = now)
    products = models.ManyToManyField('product.Product', through='OrderItem', related_name='orders')

    def __str__(self):
        return "Order made by {0} at {1}".format(self.user, self.order_date)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('order', 'product')
