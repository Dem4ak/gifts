from django.shortcuts import render

from products.models import Product, ProductCategory


def all_products(request, category_slug):
    category = ProductCategory.objects.get(slug=category_slug)
    return render(request, 'products/category.html', locals())


def one_product(request, product_slug, category_slug):
    product = Product.objects.get(slug=product_slug)
    return render(request, 'products/product.html', locals())