from django.conf import settings
from django.utils.timezone import now
from django.db import models
from order.models import Order

class Invoice(models.Model):    
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE
    )
    billing_name = models.CharField(max_length=200, null= False)
    billing_address = models.CharField(max_length=200, null= False)
    billing_ssn = models.CharField(max_length=100, null= False)
    invoice_datetime = models.DateTimeField(default = now)

    def __str__(self):
        return "Invoice made for order {0}".format(self.order)