from django.db.models import Avg
from django.shortcuts import render

from products.models import Product, Category, ProductReview, ProductToCategory


def all_products(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = ProductToCategory.objects.filter(category=category.id)
    subcategory = Category.objects.filter(parent=category.id)
    return render(request, 'products/category.html', locals())


def one_product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    average_rating = ProductReview.objects.filter(product=product.id).aggregate(Avg('rating')).values()
    related_products = Product.objects.filter(category=product.category_id)[:5]
    reviews_product = ProductReview.objects.filter(product=product.id)
    group_products_count = Product.objects.filter(group_id=product.group_id).count()
    group_products = Product.objects.filter(group_id=product.group_id)
    return render(request, 'products/product.html', locals())
