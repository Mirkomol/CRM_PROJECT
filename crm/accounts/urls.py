from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('products/', views.Products, name='products'),
    path('customers/<int:pk>/', views.Customers, name='customers'),
    path('create_order/', views.createOrder, name='create_order'),
    path('create_customer/', views.createCustomer, name='create_customer'),
    path('create_product/', views.createProduct, name='create_product'),
]
