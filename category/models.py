from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null= False)
    description = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, null= False) 

    def __str__(self):
        return self.name
