from django.db import models
from users.models import User

# Create your models here.

class Product(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, unique=True)
    product_code = models.CharField(max_length=50, blank=True)
    # Pendiente función categoría
    product_category = models.CharField(max_length=20)
    unit_price = models.FloatField(default=0)
    description = models.CharField(max_length=250, blank=True)
    product_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product_name}'
