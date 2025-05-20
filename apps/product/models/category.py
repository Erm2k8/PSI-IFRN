from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return f"Category: {self.name}"