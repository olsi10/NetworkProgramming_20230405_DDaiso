from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from product.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    # 보여줄 거는 프로덕트다.
    # 'product_list', {'product_list' : Product.object.all() }
    paginate_by = 2

class ProductDetailView(DetailView):
    model = Product
    # 'product_detail.html', { 'product' : Product.object.get(pk=pk) } pk -> primary key

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price']      # '__all__' 으로도 할 수 있다.
    template_name_suffix = '_create'     # product_form.html -> product_create.html
    success_url = reverse_lazy('product:list')    # 추가 성공하면, 이동할 url 이름

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price'] # '__all__'
    template_name_suffix = '_update' # product_form.html -> product_update.html 뒤에 달리는 프리픽스는 앞에 뒤에는 서픽스
    # 일반적으로 성공하면 detail로 간다
    # success_url = reverse_lazy('product:list') # 수정 성공하면, 이동할 url 이름

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:list') # 삭제 성공하면 이동할 url 이동
    # product_confirm_delete.hmtl 서픽스로 정해짐