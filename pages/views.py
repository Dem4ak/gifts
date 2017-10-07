from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from pages.models import Page


def page(request, slug):
    page = Page.objects.get(slug=slug)
    return render(request, 'pages/page.html', locals())
