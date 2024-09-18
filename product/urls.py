from django.urls import path
from . import views

app_name = "product"
urlpatterns = [
    path('', views.view_product, name='products'),
    path('product_detail/<int:prod_id>/', views.product_detail, name='product_detail'),
]
