from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('add_product/', views.ProductCreateView.as_view(), name='add_product'),
]
