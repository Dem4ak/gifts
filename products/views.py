from django.shortcuts import render

from products.models import Product, Category


def all_products(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=category.id)
    subcategory = Category.objects.filter(parent=category.id)
    return render(request, 'products/category.html', locals())


def one_product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    group_products_count = Product.objects.filter(group_id=product.group_id).count()
    group_products = Product.objects.filter(group_id=product.group_id)
    return render(request, 'products/product.html', locals())
