from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

class Product(models.Model): # 열에 들어감
    name = models.CharField(max_length=20)
    # price = models.PositiveSmallIntegerField(0)
    price = models.IntegerField(validators=[MinValueValidator(0)])
