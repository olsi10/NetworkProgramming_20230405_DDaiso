from django.shortcuts import render
from django.views.generic import ListView

from product.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product # 보여줄 거는 프로덕트다.
