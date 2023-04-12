from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [ # 프로덕트 리스트뷰를 호출하는구나~~~
    path('list/', views.ProductListView.as_view(), name='list'), # product : list
]