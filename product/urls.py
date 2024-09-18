from django.urls import path
from . import views

app_name = "product"
urlpatterns = [
    path('', views.view_product, name='products'),
]
