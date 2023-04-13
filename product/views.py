from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    # 보여줄 거는 프로덕트다.
    # 'product_list', {'product_list' : Product.object.all() }

class ProductDetailView(DetailView):
    model = Product
    # 'product_detail.html', { 'product' : Product.object.get(pk=pk) } pk -> primary key