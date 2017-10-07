from news.models import News
from pages.models import Page
from gift_ru.models import *
from products.models import ProductCategory, ProductImage
from django.shortcuts import render
from works.models import WorksImage


def home(request):
    menu = Page.objects.filter(show_in_header=True)
    slider = SliderImage.objects.all()
    category = ProductCategory.objects.filter(parent_id=25)
    steps = StepBy.objects.all().order_by('sort')
    new_products = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    seo_text = Home.objects.get(id=1)
    news = News.objects.filter(category=1)[:5]
    big_works = WorksImage.objects.filter(is_big=True)[:2]
    small_works = WorksImage.objects.exclude(is_big=True)[:4]
    return render(request, 'home/home.html', locals())
