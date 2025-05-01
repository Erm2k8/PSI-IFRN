from email.policy import default
from django.db import models

class Product(models.Model):
    class Categories(models.TextChoices):
        PERIPHERAL = 'Peripheral'
        COMPONENT = 'Component'
        ACCESSORIE = 'Accessorie'
    
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
        max_length=20,
        null=False,
        blank=False,
        choices=Categories.choices,
        default=Categories.COMPONENT
    )

from django import forms

class RegisterProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['description', 'price', 'category']