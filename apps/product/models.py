from django.db import models

class Product(models.Model):
    class Categories(models.TextChoices):
        PER = 'Peripheral'
        COM = 'Component'
        ACC = 'Accessorie'
    
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
        default=Categories.COM
    )

    image = models.ImageField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.id} - {self.category}, {self.description}, {self.price}'
