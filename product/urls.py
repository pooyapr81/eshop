from django.urls import path
from . import views

app_name = "product"
urlpatterns = [
    path('', views.view_product, name='products'),
    path('product_detail/<int:prod_id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('checkout/', views.checkout, name="checkout"),
]
