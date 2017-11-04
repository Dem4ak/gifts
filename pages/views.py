from django.shortcuts import render
from pages.models import Page


def page(request, slug):
    page = Page.objects.get(slug=slug)
    child_pages = Page.objects.filter(parent=page.id).order_by('order')
    return render(request, 'pages/page.html', locals())
