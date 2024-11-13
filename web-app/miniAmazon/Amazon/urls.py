from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path("user_register/", views.user_register, name="user_register"),
    path("product_list/", views.product_list, name="product_list"),
    path("cart/", views.cart, name="cart"),
    path('submit_order/', views.submit_order, name='submit_order'),
    path('query_order/', views.query_order, name='query_order'),
    path('order-status/<int:order_id>/', views.order_status, name='order_status'),
    path('change_destination/', views.change_destination, name='change_destination'),
]
