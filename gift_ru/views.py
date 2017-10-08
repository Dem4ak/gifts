from news.models import News
from gift_ru.models import *
from products.models import ProductCategory, ProductImage, Product
from django.shortcuts import render
from works.models import WorksImage


def home(request):
    slider = SliderImage.objects.all()
    category = ProductCategory.objects.filter(parent_id=25)
    steps = StepBy.objects.all().order_by('sort')
    new_products = Product.objects.filter(is_active=True)[0:6]
    seo_text = Home.objects.get(id=1)
    news = News.objects.filter(category=1)[:5]
    big_works = WorksImage.objects.filter(is_big=True)[:2]
    small_works = WorksImage.objects.exclude(is_big=True)[:4]
    return render(request, 'home/home.html', locals())
