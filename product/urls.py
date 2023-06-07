from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [ # 프로덕트 리스트뷰를 호출하는구나~~~
    path('list/', views.ProductListView.as_view(), name='list'), # product : list
    # list2로 url들어오면 list_prodict라는 함수 호출해!!!!!!!라는 코드, 리턴값이 함수인거야
    path('list2/', views.list_product, name='list2'), # product : list2
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail'), # product : detail
    path('detail2/<int:pk>/', views.detail_product, name='detail2'), # product : detail2
    path('add/', views.ProductCreateView.as_view(), name='add'),
    path('add2/', views.create_product, name='add2'), # product:add2
    path('edit/<int:pk>/', views.ProductUpdateView.as_view(), name='edit'), # product:edit
    path('edit2/<int:pk>/', views.update_product, name='edit2'), # product:edit
    path('remove/<int:pk>/', views.ProductDeleteView.as_view(), name='remove') # product:remove

]