from django.shortcuts import render
from .models import Product


def view_product(request):
    context = {}
    products = Product.objects.all()

    context['products'] = products

    return render(request, 'product/products.html', context)

