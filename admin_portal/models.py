from django.db import models
from django import forms
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Product (models.Model):
    class Category(models.TextChoices):
        KIDS = 'KD', _('KIDS')
        ADULTS = 'AD', _('ADULTS')

    product_id = models.CharField(max_length=75)
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=150)
    image = models.ImageField(default='default.jpg', upload_to='product_pics')
    price = models.CharField(max_length=50)
    category =  models.CharField(
        max_length=2,
        choices=Category.choices,
        default=Category.KIDS,
    )
    def __str__(self):
        return f'Product - {self.title}'