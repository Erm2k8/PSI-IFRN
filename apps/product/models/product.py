from django.db import models
from .category import Category

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='category',
        null=True,
        blank=True,
    )
    
    description = models.CharField(
        max_length=1023,
        null=False,
        blank=False,
    )
    
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="products/"
    )

    def __str__(self):
        return f'{self.id} - {self.category}, {self.description}, {self.price}'
