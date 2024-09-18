from django.shortcuts import render
from .models import Product, Cart


def view_product(request):
    context = {}
    products = Product.objects.all()

    context['products'] = products

    return render(request, 'product/products.html', context)


def product_detail(request, prod_id):
    context = {}
    product = Product.objects.get(id=prod_id)

    context['product'] = product

    return render(request, 'product/product_detail.html', context)