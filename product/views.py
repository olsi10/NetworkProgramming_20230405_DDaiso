from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from product.forms import ProductCreationForm, ProductChangeForm
from product.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    # 보여줄 거는 프로덕트다.
    # 'product_list', {'product_list' : Product.object.all() }
    paginate_by = 2

def list_product(request):
    product_list = Product.objects.all() # DB에 있는 product 전체 가져오자 all()[:2] 두개보고싶으면 이렇게
    context = {'product_list': product_list} # product_list 라는 키로 놓자
    return render(request, 'product/product_list.html', context) # product/product_list.html에 보내자

class ProductDetailView(DetailView):
    model = Product
    # 'product_detail.html', { 'product' : Product.object.get(pk=pk) } pk -> primary key

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price']      # '__all__' 으로도 할 수 있다.
    template_name_suffix = '_create'     # product_form.html -> product_create.html
    success_url = reverse_lazy('product:list')    # 추가 성공하면, 이동할 url 이름

def create_product(request):
    if request.method == 'POST': # 사용자가 입력하고 submit 버튼 눌렀을 때
        form = ProductCreationForm(request.POST) # 입력하 내용이 이 변수에 들어감
        if form.is_valid(): # form을 검사하자
            form.save()     # form에 있는 정보를 저장하자
        return redirect('product:list2') # 저장 하고 product_list2로 넘어가자
    else: # 처음에 빈 폼 보여주자
        form = ProductCreationForm
    return render(request, 'product/product_create.html', {'form' : form})

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price'] # '__all__'
    template_name_suffix = '_update' # product_form.html -> product_update.html 뒤에 달리는 프리픽스는 앞에 뒤에는 서픽스
    # 일반적으로 성공하면 detail로 간다
    # success_url = reverse_lazy('product:list') # 수정 성공하면, 이동할 url 이름

def update_product(request, pk):
    if request.method == 'POST': # 사용자가 입력하고 submit 버튼 눌렀을 때
        form = ProductChangeForm(request.POST) # form에 있는 내용 가져오자
        if form.is_valid(): # form 검사하자
            selected_product = Product.objects.get(pk=pk) # pk로 Product에서 하나 꺼내자
            selected_product.name =  form.cleaned_data.get('name') # 입력한 내용으로 product 수정하자
            selected_product.price = form.cleaned_data.get('price')
            selected_product.save()
        return redirect('product:detail2', pk=pk)# 이동~!

        # product 저장
    else: # 처음에 입력한 내용을 폼으로 보여주자
        selected_product = Product.objects.get(pk=pk) # pk로 Product에서 하나 꺼내자
        form = ProductChangeForm(instance=selected_product) # form에 표시하자
    return render(request, 'product/product_update.html', {'form' : form})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:list') # 삭제 성공하면 이동할 url 이동
    # product_confirm_delete.hmtl 서픽스로 정해짐
    # 장고가 pk 자동으로 넣어줌
def detail_product(request, pk):
    # filter는 조건에 맞춰서 가져오는 것
    product = Product.objects.get(pk=pk) # db에서 pk가 pk인 product 하나 가져오자
    context = {'product': product} # product라는 키로 놓자
    return render(request, 'product/product_detail.html', context) # product_detail.html에게 product라는 번수로 product를 보내자
