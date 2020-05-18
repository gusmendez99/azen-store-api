from django.conf import settings
from django.utils.timezone import now
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from invoice.models import Invoice

class Payment(models.Model):    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    invoice = models.OneToOneField(
        Invoice,
        on_delete=models.CASCADE
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.01, validators=[MinValueValidator(Decimal('0.01'))])
    payment_date = models.DateTimeField(default = now)

    def __str__(self):
        return "Payment made by {0} at {1} with ammount {2}".format(self.user, self.payment_date, self.amount)
