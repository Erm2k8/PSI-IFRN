from email.policy import default
from django.db import models

class Product(models.Model):
    class Categories(models.TextChoices):
        PERIPHERALS = 'PER'
        COMPONENTS = 'COM'
        ACCESSORIES = 'ACC'
    
    description = models.CharField(
        max_length=1023,
        null=False,
        blank=False,
    )
    
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    
    category = models.CharField(
        max_length=3,
        null=False,
        blank=False,
        choices=Categories.choices,
        default=Categories.COMPONENTS
    )
