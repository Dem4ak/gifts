from django.shortcuts import render

from news.models import News, NewsCategory


def all_news(request):
    all_news = News.objects.filter(category=1)
    return render(request, 'news/news_list.html', locals())


def one_news(request, slug):
    news = News.objects.get(slug=slug)
    return render(request, 'news/one_news.html', locals())
