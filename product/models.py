from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

class Product(models.Model): # 열에 들어감
    name = models.CharField(max_length=20)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    # price = models.PositiveIntegerField(0)

    def __str__(self):
        return f'{self.name} : {self.price}'