from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Avg
from django.shortcuts import render, render_to_response

from products.models import Product, Category, ProductReview, ProductToCategory


def all_products(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products = ProductToCategory.objects.filter(category=category.id)
    subcategory = Category.objects.filter(parent=category.id)
    paginator = Paginator(products, 30)  # Show 30 contacts per page
    page = request.GET.get('page')
    see_more = Category.objects.filter(parent=category.parent)[:7]
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    return render_to_response('products/category.html',
                              {"products": products, "category": category, "subcategory": subcategory,
                               "see_more": see_more,
                               "paginator": paginator})


def one_product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    average_rating = ProductReview.objects.filter(product=product.id).aggregate(Avg('rating')).values()
    related_products = Product.objects.filter(category=product.category_id)[:5]
    reviews_product = ProductReview.objects.filter(product=product.id)
    group_products_count = Product.objects.filter(group_id=product.group_id).count()
    group_products = Product.objects.filter(group_id=product.group_id)
    return render(request, 'products/product.html', locals())
